import pandas as pd
from docxtpl import DocxTemplate

file =('table/table.xlsx')
newdata = pd.read_excel(file)
print(newdata)

#Dict (to populate table)
context = {'tbl_contents': []}

tpl = DocxTemplate('table/sample.docx')

def tab():
    for index, row in newdata.iterrows():
        sam = {'cols': list(row)}
        context['tbl_contents'].append(sam)
    tpl.render(context)
    tpl.save('table/output.docx')
tab()


