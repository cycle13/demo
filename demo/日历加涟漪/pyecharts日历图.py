import pandas as pd
import json
from datetime import datetime


def excel_one_line_to_list():
    df = pd.read_excel("demo.xlsx", usecols=[0],names=None)
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[0])
    return result

def data_range():
    xl = pd.date_range('1/1/2019','12/31/2019')
    date_list = [datetime.strftime(x,'%F') for x in xl]
    return date_list


if __name__ == '__main__':
    data = data_range()
    excel = excel_one_line_to_list()
    dtat = []
    for i in range(0,len(data)):
        dtat.append([data[i],excel[i]])
    with open('beijing1.json', 'w') as file_obj:
        json.dump(dtat, file_obj)
