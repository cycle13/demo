import json

from pyecharts import options as opts
from pyecharts.charts import Graph


with open("合川_颗粒物.json", "r", encoding="utf-8") as f:
    j = json.load(f)
    nodes = j["nodes"]
    links = j["links"]
    categories = j["categories"]

c = (
    Graph(init_opts=opts.InitOpts(width="1600px", height="1000px"))
    .add(
        "",
        nodes=nodes,
        links=links,
        categories=categories,
        layout="circular",
        is_rotate_label=True,
        repulsion=4000,
        gravity=0.1,
        linestyle_opts=opts.LineStyleOpts(color="source", curve=0.3),
        label_opts=opts.LabelOpts(position="right"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="合川各乡镇与各行业颗粒物排放关系图"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_left="4%", pos_top="3%"),
    )
    .render("合川各乡镇与各行业颗粒物排放关系图.html")
)
c