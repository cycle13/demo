from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt


def pic_tab(document,text):
#表头样式设计
    paragraph = document.add_paragraph()
    paragraph.add_run(text).font.size = Pt(10.5)
    paragraph_format = paragraph.paragraph_format
    paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph_format.space_before = Pt(2)                   #段前段后间距设置
    paragraph_format.space_after = Pt(2)