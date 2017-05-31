# -*- coding:utf-8 -*-

import openpyxl




class ReplyText(object):

    def __init__(self, xlsxfile):
        self.xlsxfile = xlsxfile
        self.sheet = self.readfile(xlsxfile)

    def readfile(self, xlsxfile):
        wb = openpyxl.load_workbook(self.xlsxfile)
        sheet = wb.get_active_sheet()
        return sheet

    def get_allrows(self):
        first_row = 2
        for item in self.sheet[first_row:self.sheet.max_row]:
            yield (item[0].value, item[1].value)


if __name__ == '__main__':
    reply_text = ReplyText("雅思资料.xlsx")
    result = reply_text.get_allrows()
    print(tuple(result))
