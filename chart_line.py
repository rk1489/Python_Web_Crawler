import xlsxwriter

workbook=xlsxwriter.Workbook("chart_line.xlsx")
worksheet=workbook.add_worksheet()
bold=workbook.add_format({"bold":1})

headings=["Number","Batch 1","Batch 2"]
data=[
    [20,30,40,50,60,70],
    [10,20,30,40,50,60],
    [30,40,50,60,70,80],
]

worksheet.write_row('A1',headings,bold)
worksheet.write_column('A2',data[0])
worksheet.write_column('B2',data[1])
worksheet.write_column('C2',data[2])


chart1=workbook.add_chart({'type':'bar'})

chart1.add_series({
    'name': '=Sheet1!$B$1',
    'categories': '=Sheet1!$A$2:$A$7',
    'values':  '=Sheet1!$B$2:$B$7',
})

chart1.add_series({
    'name': ['Sheet1',0,2],
    'categories': ['Sheet1',1,0,6,0],
    'values':  ['Sheet1',1,2,6,2],
})

chart1.set_title({'name': 'Results of Sample Analysis'})
chart1.set_x_axis({'name': 'Test No.'})
chart1.set_y_axis({'name': 'Sample Length(mm)'})


chart1.set_style(10)

worksheet.insert_chart('D2',chart1,{'x_offset':25,'y_offset':10})
workbook.close()











