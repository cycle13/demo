import pandas as pd
from pandasgui import show

df = pd.read_excel('all_data.xls')
show(df,settings={'block':True})