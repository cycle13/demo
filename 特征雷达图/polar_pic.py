import data_visual
import data_opt
import spider_data
from datetime import datetime
import datetime as datatime




yestoday = (datetime.now() + datatime.timedelta(days=-1)).strftime("%Y-%m-%d %H")
file_dir = 'excelfile/' + yestoday + '.xls'
newfile_dir = 'excelfile/' + yestoday + '.xlsx'
# 获取数据
# spider_data.save_excel(file_dir)
for now_time in ["商水县","太康县","扶沟县",'沈丘县','淮阳县','西华县','郸城县','项城市','鹿邑县']:
    name = data_opt.tezheng(file_dir,newfile_dir,now_time)
    data_visual.plot_radar(newfile_dir,now_time,name)