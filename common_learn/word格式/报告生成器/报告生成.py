from docx import Document
from docx.shared import Inches
from zhengwen import zw
from pic_tab import pic_tab
import headings
import tabless
import pictur
from head_foot import hed_fot




document = Document()                                     #创建段落

headings.headings1(document,"应用场景示例")

# # 添加分页符
# document.add_page_break()


#正文样式设计
tet = r'在推动立法的同时，《指导意见》要求，各地抓紧制定2030' \
      r'年前二氧化碳排放达峰行动方案，综合运用相关政策工具和手段措施，' \
      r'持续推动实施。“各地要结合实际提出积极明确的达峰目标，制定' \
      r'达峰实施方案和配套措施。”《指导意见》鼓励能源、工业、交通、建' \
      r'筑等重点领域制定达峰专项方案。推动钢铁、建材、有色、化工、石化、' \
      r'电力、煤炭等重点行业提出明确的达峰目标并制定达峰行动方案。此外，还' \
      r'将通过规划环评、项目环评推动区域、行业和企业落实煤炭消费削减替代、温' \
      r'室气体排放控制等政策要求，推动将气候变化影响纳入环境影响评价。'
zw(document,tet)

headings.headings2(document,"表格")

pic_tab(document,'表1  表格')
list = ['第一行第一列', '第一行第二列', '第一行第三列','第一行第四列', '第一行第五列', '第一行第六列','0', '1','2','3','4','5','6', '7','8','9','10','11']
table_style = 'Table Grid'
tabless.tabless(3,6,document,list,table_style)

headings.headings3(document,"图")

#插入图片样式设计
document.add_picture('data/demo.png', width=Inches(6))   #调整图片大小
#表格图设计
pic_tab(document,'图1  图')

headings.headings3(document,"图表")

path = r'D:\pycharm\常规学习\CMAQ可视化\pic\CO\20210131'
pictur.pics(path,document,table_style,3,2)
pic_tab(document,'图2  图')

#页眉页脚
headtext = '日报'
footext = '生态环境研究院'
hed_fot(document,headtext,footext)






document.save('file/demo.docx')