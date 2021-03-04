from openpyxl import Workbook,load_workbook
import os


start = int(input("从第几个单词开始："))
end = int(input("到第几个单词结束："))


wb = load_workbook('专升本单词.xlsx')
sheet = wb.active
times = 0
for index,row in enumerate(sheet):
    if index >= start and index<end:
        times+=1
        with open('../源码1/每日单词.txt','a',encoding = 'utf-8')as file:
            file.write(row[0].value + '\n')
            print('写入成功！')
print(f'一共{times}个单词')

