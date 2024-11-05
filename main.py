from fpdf import FPDF
import pandas as pd
df=pd.read_csv('topics.csv')

#unit='mm' means all dimensions will be in millimeters

pdf=FPDF(orientation='P', unit='mm', format='A4')
for index,item in df.iterrows():

    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100,100,100)
    # ln=1 --> ln is actually a break of line --> Go to next line
    pdf.cell(w=0, h=12, txt=item[1], align='L')
    pdf.line(10,21,200,21)





pdf.output('output.pdf')