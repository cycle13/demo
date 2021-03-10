import requests
import os
import time
import pandas as pd



session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
urls = ['https://sprintars.riam.kyushu-u.ac.jp/images_asia/y{0}/con/conbc_sfc_asia_{1}{2}{3}.png','https://sprintars.riam.kyushu-u.ac.jp/images_asia/y{0}/con/conoc_sfc_asia_{1}{2}{3}.png','https://sprintars.riam.kyushu-u.ac.jp/images_asia/y{0}/con/consu_sfc_asia_{1}{2}{3}.png','https://sprintars.riam.kyushu-u.ac.jp/images_asia/y{0}/con/condu_sfc_asia_{1}{2}{3}.png','https://sprintars.riam.kyushu-u.ac.jp/images_asia/y{0}/con/consa_sfc_asia_{1}{2}{3}.png','https://sprintars.riam.kyushu-u.ac.jp/images_asia/y{0}/con/pm25_sfc_asia_{1}{2}{3}.png','https://sprintars.riam.kyushu-u.ac.jp/images_asia/y{0}/con/pm10_sfc_asia_{1}{2}{3}.png','https://sprintars.riam.kyushu-u.ac.jp/images_asia/y{0}/con/pptso2_sfc_asia_{1}{2}{3}.png','https://sprintars.riam.kyushu-u.ac.jp/images_asia/y{0}/con/pptdms_sfc_asia_{1}{2}{3}.png']
mouth = {'01':'JAN','02':'FEB','03':'MAR','04':'APR','05':'MAY','06':'JUN','07':'JUL','08':'AUG','09':'SEP','10':'OCT','11':'NOV','12':'DEC',}
begin = '1980-01-01'
end = '1980-01-03'
time_range = [x.strftime('%Y-%m-%d') for x in list(pd.date_range(start=begin, end=end))]
for i in time_range:
    time.sleep(2)
    for j in urls:
        url = j.format(i[0:4],i[0:4],mouth[i[5:7]],i[8:10])
        print(url)
        res = session.get(url,headers=headers)
        if not os.path.exists('data/'+i):
            os.makedirs('data/'+i)
        with open('data/'+ i +'/'+ url[60:-4] + '.png', 'wb') as f:
            f.write(res.content)
