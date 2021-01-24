from pyecharts import options as opts
from pyecharts.charts import BMap, Timeline


tl = Timeline(init_opts=opts.InitOpts(width="1000px", height="600px"))
provinces = [['广东', '北京', '上海', '江西', '湖南', '浙江', '江苏'],
             ['广东', '北京', '上海', '江西', '湖南', '浙江', '江苏'],
             ['广东', '北京', '上海', '江西', '湖南', '浙江', '江苏'],
             ['广东', '北京', '上海', '江西', '湖南', '浙江', '江苏'],
             ['广东', '北京', '上海', '江西', '湖南', '浙江', '江苏']]
valuesdata = [[21, 79, 141, 36, 41, 94, 126],
            [126, 137, 81, 62, 35, 133, 56],
            [21, 128, 110, 125, 118, 117, 109],
            [127, 110, 146, 132, 57, 96, 45],
            [116, 52, 20, 63, 24, 32, 46]]
tl.add_schema(pos_left="50%", pos_right="10px", pos_bottom="15px")
for i in range(2015, 2020):
    bmap = (
        BMap(init_opts=opts.InitOpts(width="1600px", height="1000px"))
        .add_schema(baidu_ak="TaXHPPc7HlxpjOFL3XjakmvHMbhp8YdX", center=[120.13066322374, 30.240018034923])
        .add(
            "bmap",
            [list(z) for z in zip(provinces[i-2015], valuesdata[i-2015])],
            type_="heatmap",
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Timeline-BMap-热力图-{}年".format(i)),
            visualmap_opts=opts.VisualMapOpts(pos_bottom="center", pos_right="10px"),
            tooltip_opts=opts.TooltipOpts(formatter=None),
        )
    )
    tl.add(bmap, "{}年".format(i))
tl.render("timeline_bmap.html")