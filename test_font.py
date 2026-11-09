from fpdf import FPDF
pdf = FPDF()
try:
    pdf.add_font('Montserrat', '', 'C:/Users/HP OMEN/AppData/Local/hermes/work/fonts/Montserrat-Variable.ttf')
    print('Font registered successfully')
    pdf.add_page()
    pdf.set_font('Montserrat', '', 12)
    pdf.cell(0, 10, 'Test Montserrat', align='C')
    pdf.ln(10)
    pdf.output('C:/Users/HP OMEN/AppData/Local/hermes/work/font_test.pdf')
    print('PDF generated successfully')
except Exception as e:
    print(f'Error: {e}')
    import traceback
    traceback.print_exc()
