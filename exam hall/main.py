import xlsxwriter
import xlrd


examcan = int(input("how many stud in one exam"))

examhall = int(input("how many  exam hall"))



col= int(input("how many exam col"))



global list
list=[]
loc = ("input.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 
for i in range(sheet.nrows): 
    list.append(sheet.cell_value(i, 0))
print (list)

listlen=len(list)
print(listlen)
if(examhall<(listlen/examcan)) :
	print("error")

else :
	for i in list:
			workbook = xlsxwriter.Workbook('output.xlsx')
			worksheet = workbook.add_worksheet()
			row = 0
			column = 0
			k=0;
			c=0
			for item in list :
				worksheet.write(row, column, item)
				row += 1
				k+=1
				if k%col==0 :
					column+=1
					row=c
					
				if k%examcan==0 :
					column=0
					row+=col+1
					c=row

				

			workbook.close()	