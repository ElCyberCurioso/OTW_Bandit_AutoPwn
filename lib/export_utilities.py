import pandas as pd
from fpdf import FPDF
import time

import lib.data_utilities as data_utilities
import lib.local_utilities as local_utilities
import lib.utilities as utilities
import lib.constants as constants

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

def _prepare_export_filename(filename, users, extension, export_folder=constants.EXPORT_FOLDER):
    """
    Función helper para preparar el nombre del archivo de exportación.
    Retorna (filepath, file_exists)
    """
    # Añadir sufijo según usuarios
    suffix = "all_users" if utilities.count_elements(users) > 1 else users
    filename = f"{filename}_{suffix}"
    
    # Añadir extensión si no la tiene
    if not filename.endswith(extension):
        filename = f"{filename}{extension}"
    
    # Verificar si el archivo existe
    _, _, file_exists = local_utilities.check_file_exists(__file__, filename, file_directory=export_folder)
    
    if file_exists:
        print("\nFile exist already!")
        time.sleep(1)
        return None, True
    
    return f"{export_folder}/{filename}", False

# Method that manages PDF exports
def manage_pdf(df, filename, users, export_folder=constants.EXPORT_FOLDER):
    filepath, file_exists = _prepare_export_filename(filename, users, ".pdf", export_folder)
    if file_exists:
        return
    
    print(f"​\nExporting to PDF: {filepath}")
    export_to_pdf(df, filepath)

# Method that manages Excel exports
def manage_excel(df, filename, users, export_folder=constants.EXPORT_FOLDER):
    filepath, file_exists = _prepare_export_filename(filename, users, ".xlsx", export_folder)
    if file_exists:
        return
    
    print(f"​\nExporting to Excel: {filepath}")
    export_to_excel(df, filepath)

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