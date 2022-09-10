# Import Module
from win32com import client
from openpyxl import Workbook, load_workbook
import os
import datetime


def strrr():
    a = str(datetime.datetime.now().date())
    return a


path = os.path.join(os.getcwd(), strrr())
print(path)
try:
    os.mkdir(path)
except (Exception, FileExistsError) as e:
    print(e)



# Open Microsoft Excel
excel = client.Dispatch("Excel.Application")

exfile = r'C:\Users\MNN-068\OneDrive\Desktop\Sep(01-09-2022)\D_Bar_Report.xlsx'

# Read Excel File
sheets = excel.Workbooks.Open(exfile)

wb = load_workbook(exfile)
for i in wb:
    if i.title == 'D-Bars':
        continue
    elif i.title == 'Summery':
        continue
    work_sheets = sheets.Worksheets[i.title]
    print(i.title)

    # Convert into PDF File
    work_sheets.ExportAsFixedFormat(0, f'{path}\\{i.title}.pdf')

