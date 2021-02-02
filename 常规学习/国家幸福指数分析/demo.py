import numpy as np
import pandas as pd
import os,sys
import matplotlib.pyplot as plt
import seaborn as sns
import plotly as py
import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import init_notebook_mode, iplot, plot

#数列的路径
# file_path = os.path.dirname(os.path.abspath(__file__))
file_path = 'data'
file_path1 = 'pic'

# 读入数据
df_2015 = pd.read_csv(f'{file_path}/2015.csv')
df_2016 = pd.read_csv(f'{file_path}/2016.csv')
df_2017 = pd.read_csv(f'{file_path}/2017.csv')
df_2018 = pd.read_csv(f'{file_path}/2018.csv')
df_2019 = pd.read_csv(f'{file_path}/2019.csv')

# 新增列-年份
df_2015["year"] = str(2015)
df_2016["year"] = str(2016)
df_2017["year"] = str(2017)
df_2018["year"] = str(2018)
df_2019["year"] = str(2019)

# 合并数据
df_all = df_2015.append([df_2016, df_2017, df_2018, df_2019], sort=False)
df_all.drop('Unnamed: 0', axis=1, inplace=True)
df_all.head()
data = dict(type='choropleth',
            locations=df_2019['region'],
            locationmode='country names',
            colorscale='RdYlGn',
            z=df_2019['happiness'],
            text=df_2019['region'],
            colorbar={'title': '幸福指数'})

# layout = dict(title='2019年世界幸福指数地图',
#               geo=dict(showframe=True, projection={'type': 'azimuthal equal area'}))

# choromap3 = go.Figure(data=[data], layout=layout)
# plot(choromap3, filename=f'{file_path}/世界幸福地图.html')

# # 合并数据
# rank_top10 = df_2019.head(10)[['rank', 'region', 'happiness']]
# last_top10 = df_2019.tail(10)[['rank', 'region', 'happiness']]
# rank_concat = pd.concat([rank_top10, last_top10])

# # 条形图
# fig = px.bar(rank_concat,
#              x="region",
#              y="happiness",
#              color="region",
#              title="2019年全球最幸福和最不幸福的国家")

# plot(fig, filename=f'{file_path}/2019世界幸福国家排行Top10和Last10.html')

# 热力图
# plt.figure(figsize=(25, 20))
# sns.heatmap(df_all.corr(), cmap='rainbow', linewidths=0.1, annot=True)
# plt.title('数值变量之间的相关性', fontsize=18)
# plt.xticks(fontsize=13)
# plt.yticks(fontsize=13)
# plt.show()

# # 散点图
# fig = px.scatter(df_all, x='gdp_per_capita',
#                  y='happiness',
#                  facet_row='year',
#                  color='year',
#                  # trendline='ols'
#                  )
# fig.update_layout(height=800, title_text='人均GDP和幸福指数')
# plot(fig, filename=f'{file_path1}/GDP和幸福得分.html')

# # 散点图
fig = px.scatter(df_all, x='healthy_life_expectancy',
                 y='happiness',
                 facet_row='year',
                 color='year',
                 # trendline='ols'
                 )
fig.update_layout(
    height=800, title_text='健康预期寿命和幸福指数')
plot(fig, filename=f'{file_path1}/健康预期寿命和幸福得分.html')

# #散点图
# fig = px.scatter(df_all, x='freedom_to_life_choise',
#                  y='happiness',
#                  facet_row='year',
#                  color='year',
#                  trendline='ols'
#                  )
# fig.update_layout(
#     height=800, title_text='自由权和幸福指数')
# plot(fig, filename=f'{file_path}/自由权和幸福得分.html')

# #散点图
# fig = px.scatter(df_all, x='corruption_perceptions',
#                  y='happiness',
#                  facet_row='year',
#                  color='year',
#                  trendline='ols'
#                  )
# fig.update_layout(
#     height=800, title_text='清廉指数和幸福指数')
# plot(fig, filename=f'{file_path}/清廉指数和幸福得分.html')

# #散点图
# fig = px.scatter(df_all, x='generosity',
#                  y='happiness',
#                  facet_row='year',
#                  color='year',
#                  trendline='ols'
#                  )
# fig.update_layout(
#     height=800, title_text='慷慨程度和幸福指数')
# plot(fig, filename=f'{file_path}/慷慨程度和幸福得分.html')

# #散点图
# fig = px.scatter(df_all, x='social_support',
#                  y='happiness',
#                  facet_row='year',
#                  color='year',
#                  trendline='ols'
#                  )
# fig.update_layout(
#     height=800, title_text='社会援助和幸福指数')
# plot(fig, filename=f'{file_path}/社会援助和幸福得分.html')

#动态图
# fig = px.scatter(df_all,
#                  x='gdp_per_capita',
#                  y='happiness',
#                  animation_frame='year',
#                  animation_group='region',
#                  size='rank',
#                  color='region',
#                  hover_name='region',
#                  trendline='ols'
#                 )
# fig.update_layout(title_text='幸福指数vs人均GDP')
# plot(fig, filename=f'{file_path1}/GDP和幸福水平动态图展示.html')
#
# fig = px.scatter(df_all,
#                  x='healthy_life_expectancy',
#                  y='happiness',
#                  animation_frame='year',
#                  animation_group='region',
#                  size='rank',
#                  color='region',
#                  hover_name='region',
#                  trendline='ols'
#                 )
# fig.update_layout(title_text='幸福排名vs健康预期寿命')
# plot(fig, filename=f'{file_path1}/健康预期寿命和幸福水平动态图展示.html')
