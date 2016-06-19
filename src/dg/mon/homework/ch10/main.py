#!/usr/bin/python
#encoding:utf-8
import xlwt


def txt2excel(txt_filename, excel_filename):

    f = open(txt_filename)             # get file object
    line = f.readline()
    line_index = 0

    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('sheet1', cell_overwrite_ok=True)

    while line:
        print line,                 # end by ',' will ignore /r/n
        # print(line, end = '')     # can be work in Python 3

        cell_index = 0
        for cell in line.replace("\n", "").split("\t"):
            sheet1.write(line_index, cell_index, cell)
            cell_index += 1

        line = f.readline()
        line_index += 1

    f.close()
    workbook.save(excel_filename)

if __name__ == '__main__':
    txt2excel('data.txt', 'myexcel.xls')
