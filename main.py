from fpdf import FPDF
import pandas as pd
df=pd.read_csv('topics.csv')

#unit='mm' means all dimensions will be in millimeters

pdf=FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False,margin=0)

for index,item in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=item[1], align='L')
    # If I want to make my page containing many lines
    for i in range(20,298,10):
        pdf.line(10,i,200,i)

    pdf.ln(270)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=item[1], align='R')

    for i in range(item['Pages']-1):
    #for i in range(item[2]-1):
        pdf.add_page()
        #If I want to make my page containing many lines
        for i in range(20,298,10):
            pdf.line(10,i,200,i)

    pdf.ln(270)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=item[1], align='R')
pdf.output('output.pdf')