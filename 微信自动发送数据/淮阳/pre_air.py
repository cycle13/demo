import requests
import json
import time
from datetime import datetime



session = requests.Session()
first_url = 'http://1.192.88.18:18111/page/PublishingSystem/index.html'
text_url = 'http://1.192.88.18:18111/release/getReleaseText'
image_url = 'http://1.192.88.18:18065/yewushare/fore_png/{}/{}.png'


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}


def pre_air():
    res = session.get(first_url)
    res = session.get(text_url).text
    data = json.loads(res)
    for i in data:
        timeArray = time.localtime(i['predTime']/1000)
        otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
        data1 = i['pollutionSituation'][0]
        data2 = i['sevenForecast']
        data3 = i['myAdvise']

    my_datatime = datetime.strftime(datetime.now(),'%Y-%m-%d')
    for i in range(1,9):
        res = session.get(image_url.format(my_datatime,str(i)))
        with open('image_pic/'+str(i)+'.png','wb') as f:
            f.write(res.content)
    return otherStyleTime,data1,data2,data3

