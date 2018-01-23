---
title: 'Package Learning: gevent'
date: 2017-12-19 09:41:44
tags:
---

## Openpyxl

#### Terminology
- workbook: represents a excel

```py
from openpyxl import Workbook
wb = Workbook()
# Get the default active sheet, the first one
ws = wb.active
# Create new sheet, first argument is the sheet's title, second one indicate the index of the sheet.
ws2 = wb.create_sheet('Mysheet', 0)
# change the sheet's title
ws2.title = "anotherSheet"
ws3 = ws['newTitle']
# All sheet names
print(wb.sheetnames)

# Access one cell
cell = ws['A4']

```
