#coding: utf-8
import xlsxwriter

workbook = xlsxwriter.Workbook('demo1.xlsx')    #创建一个excel文件
worksheet = workbook.add_worksheet()            #创建一个工作表对象

worksheet.set_column('A:A', 20)                 #设定第一列（A）宽度为20像素
bold = workbook.add_format({'bold': True})      #定义一个加粗格式对象

worksheet.write('A1','Hello')                   #A1单元格写入Hello
worksheet.write('A2','World',bold)
worksheet.write('B2',u'中文测试',bold)

worksheet.write(2,0,32)                         #用行列表示法写入数字
worksheet.write(3,0,35.5)
worksheet.write(4,0,'=SUM(A3:A4)')

worksheet.insert_image('B5','img/bytes_io.png')
workbook.close()