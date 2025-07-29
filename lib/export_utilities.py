import pandas as pd
from fpdf import FPDF

import lib.data_utilities as data_utilities
import lib.local_utilities as local_utilities
import lib.utilities as utilities

def export_to_pdf(df, filename="output.pdf", title="Information Report"):
    pdf = FPDF()
    pdf.set_font("Arial", size=10)

    # Calculate column widths
    col_widths = []
    for col in df.columns:
        max_width = pdf.get_string_width(str(col)) + 4  # Margin
        for item in df[col]:
            item_width = pdf.get_string_width(str(item)) + 4
            if item_width > max_width:
                max_width = item_width
        col_widths.append(max_width)

    # Determine orientation
    total_table_width = sum(col_widths)
    page_width = pdf.w - 2 * pdf.l_margin  # Usable page width
    # orientation = 'P'
    if total_table_width > page_width:
        orientation = 'L'
        pdf = FPDF(orientation=orientation)
        pdf.set_font("Arial", size=10)
        # page_width = pdf.w - 2 * pdf.l_margin

    pdf.add_page()
    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, title, ln=True, align='C')
    pdf.ln(10)
    
    # Header
    pdf.set_font("Arial", 'B', 10)
    for i, col in enumerate(df.columns):
        pdf.cell(col_widths[i], 10, str(col), border=1, align='C')
    pdf.ln()

    # Rows
    pdf.set_font("Arial", size=10)
    for _, row in df.iterrows():
        for i, item in enumerate(row):
            pdf.cell(col_widths[i], 10, str(item), border=1)
        pdf.ln()

    pdf.output(filename)

def export_to_excel(data, filename="output.xlsx"):
    df = pd.DataFrame(data)
    
    df.to_excel(filename, index=False)

# Method that manages PDF exports
def manage_pdf(df, filename, users):
    if utilities.count_elements(users) > 1:
        filename = filename + "_" + "all_users"
    else:
        filename = filename + "_" + users

    if not filename.endswith(".pdf"):
        filename = filename + ".pdf"
    
    _, _, file_exists = local_utilities.check_file_exists(__file__, filename)
    if file_exists:
        print("\nFile exist already!")
        return
    
    print(f"​\nExporting to PDF: {filename}")
    export_to_pdf(df, filename)

# Method that manages Excel exports
def manage_excel(df, filename, users):
    if utilities.count_elements(users) > 1:
        filename = filename + "_" + "all_users"
    else:
        filename = filename + "_" + users
    if not filename.endswith(".xlsx"):
        filename = filename + ".xlsx"
    
    _, _, file_exists = local_utilities.check_file_exists(__file__, filename)
    if file_exists:
        print("\nFile exist already!")
        return
    
    print(f"​\nExporting to Excel: {filename}")
    export_to_excel(df, filename)

# Main export method
def export(array_selected_fields, filename, users=[], is_pdf=False, is_excel=False):
    df = data_utilities.get_custom_data_json(users=users, as_list=False, is_print=False, fields=array_selected_fields)
    
    if is_pdf or is_excel:
        if is_pdf:
            manage_pdf(df, filename, users)
        if is_excel:
            manage_excel(df, filename, users)
    else:
        print("Wrong format...")