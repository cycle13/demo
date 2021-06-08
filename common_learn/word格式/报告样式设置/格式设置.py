from docx import Document
from docx.enum.section import WD_ORIENT

doc = Document('file/new-file-name.docx')

# 获取文档所有章节
sections = doc.sections
sec0 = sections[0]        #0代表第一页

# sec0.left_margin = 914400
print('左边距：',sec0.left_margin)
# 左边距： 914400
print('右边距：',sec0.right_margin)
# 右边距： 914400
print('上边距：',sec0.top_margin)
# 上边距： 1143000
print('下边距：',sec0.bottom_margin)
# 下边距： 1143000
print('页眉边距：',sec0.header_distance)
# 页眉边距： 540385
print('页脚边距：',sec0.footer_distance)
# 页脚边距： 629920
print('页面方向：',sec0.orientation)
# 页面方向： LANDSCAPE (1)
print('页面高度：',sec0.page_height)
# 页面高度： 10657205
print('页面宽度：',sec0.page_width)

sec0.orientation = WD_ORIENT.PORTRAIT



doc.save('file/new-file-name1.docx')