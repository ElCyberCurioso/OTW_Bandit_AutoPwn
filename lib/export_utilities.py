import pandas as pd
from fpdf import FPDF

def export_to_pdf(df, filename="output.pdf", title="Reporte"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, title, ln=True, align='C')
    pdf.ln(10)
    
    # Calculate max width
    pdf.set_font("Arial", size=10)
    col_widths = []
    for col in df.columns:
        max_width = pdf.get_string_width(str(col)) + 4  # Margin
        for item in df[col]:
            item_width = pdf.get_string_width(str(item)) + 4
            if item_width > max_width:
                max_width = item_width
        col_widths.append(max_width)

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