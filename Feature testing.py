import xlsxwriter

def create_xlsx_file():
    workbook = xlsxwriter.Workbook("carousell_scrape.xlsx")
    worksheet = workbook.add_worksheet()
    # Writing headers
    worksheet.write("A1", "Description")
    worksheet.write("B1", "Price")
    worksheet.write("C1", "URL")
    worksheet.write("D1", "Image")
    return worksheet

create_xlsx_file()

worksheet