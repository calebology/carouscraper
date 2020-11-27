import xlsxwriter
import os

workbook = xlsxwriter.Workbook(os.path.join(os.path.dirname(os.path.abspath(__file__)), "test.xlsx"))
worksheet = workbook.add_worksheet()
# Writing headers
worksheet.write("A1", "Description")
worksheet.write("B1", "Price")
worksheet.write("C1", "URL")
worksheet.write("D1", "Image")


workbook.close()