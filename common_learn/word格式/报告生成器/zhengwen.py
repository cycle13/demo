from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH,WD_LINE_SPACING  #段落对齐
from docx.shared import Inches,Pt            #段落缩进
from docx.oxml.ns import qn




def zw(document,text):
    #正文字体样式
    document.styles['Normal'].font.name=u'Times New Roman'    #正文样式
    document.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')
    #正文样式设计
    paragraph = document.add_paragraph()
    paragraph.add_run(text).font.size = Pt(12)
    paragraph_format = paragraph.paragraph_format
    paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    paragraph_format.first_line_indent = Inches(0.25)        #首行缩进
    paragraph_format.space_before = Pt(2)                   #段前段后间距设置
    paragraph_format.space_after = Pt(2)
    paragraph.line_spacing_rule = WD_LINE_SPACING.EXACTLY    #固定值
    paragraph_format.line_spacing = Pt(18)                   #固定值18磅
    paragraph.line_spacing_rule = WD_LINE_SPACING.MULTIPLE   #多倍行距
    paragraph_format.line_spacing = 1.25                     #1.25倍行间距