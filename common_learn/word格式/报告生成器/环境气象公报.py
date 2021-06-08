from docx import Document
import datetime
import time
from zhengwen import zw
from pic_tab import pic_tab
import headings
import pictur
from head_foot import hed_fot
import county_aqi


document = Document()
headings.headings1(document,"环境气象公报")
tex = county_aqi.real()
for i in tex:
      zw(document, i)

document.add_page_break()
table_style = 'Table Grid'
path = r'county_image'
pictur.pics(path,document,table_style,1,4)
pic_tab(document,'图1 全国预报图')
headtext = '中央气象台环境气象公报'
footext = '佳华科技生态环境研究院'
hed_fot(document,headtext,footext)

now_time = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H')

document.save('file/{0}.docx'.format(now_time))