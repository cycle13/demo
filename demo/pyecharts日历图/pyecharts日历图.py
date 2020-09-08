import pandas as pd
from datetime import datetime
from pyecharts.options.global_options import ThemeType
from pyecharts import options as opts
from pyecharts.charts import Calendar


def excel_one_line_to_list():
    df = pd.read_excel("demo.xlsx", usecols=[0],names=None)
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[0])
    #print(len(result))
    return result

def data_range():
    xl = pd.date_range('1/1/2019','12/31/2019')
    date_list = [datetime.strftime(x,'%F') for x in xl]
    #print(len(date_list))
    return date_list

def picet(dtat):
    c=(
    Calendar(init_opts=opts.InitOpts(bg_color='rgb(255,255,255)',#背景色，可以使用rgba(255,255,255，0.2)
                                width='1200px',
                                height='300px',
                                page_title='2019年XXX污染物浓度',
                                theme=ThemeType.MACARONS))
    .add("",
         dtat,
         calendar_opts=opts.CalendarOpts(
                                         range_="2019",      #确定范围
                                         #range_="2015-02",
                                         #range_=['2015-01-01', '2015-12-31'],
                                         daylabel_opts=opts.CalendarDayLabelOpts(name_map = "cn"),      #中文显示，必须使用pyecharts1.7.1版本
                                         monthlabel_opts=opts.CalendarMonthLabelOpts(name_map = "cn"),
                                        ),
         )
    .set_global_opts(
            title_opts=opts.TitleOpts(title="2019年XXX污染物浓度",pos_left = 550),
            toolbox_opts = opts.ToolboxOpts(is_show = True),
            visualmap_opts=opts.VisualMapOpts(
            max_=10,
            min_=0,
            orient="horizontal",
            is_piecewise=True,
            split_number = 5,
            pos_top="220px",
            pos_left="450px",
            pieces=[                                             #更改区间及区间显示颜色
                {'min':0,'max':50,'label':'优','color':'#00E400'},
                {'min':51,'max':100,'label':'良','color':'#FFFF00'},
                {'min':101,'max':150,'label':'轻度污染','color':'#FF7E00'},
                {'min':151,'max':200,'label':'中度污染','color':'#FF0000'},
                {'min':201,'max':300,'label':'重度污染','color':'#99004C'},
                {'min':300,'label':'严重污染','color':'#7E0023'},
            ]
             ),
         )
     )
    c.render()


if __name__ == '__main__':
    data = data_range()
    excel = excel_one_line_to_list()
    dtat = []
    for i in range(0,len(data)):
        dtat.append([data[i],excel[i]])
    #print(dat)
    picet(dtat)