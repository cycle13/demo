import requests
import time
import urllib.request


session = requests.Session()
first_url = 'http://wxmaps.org/meteogram_custom.php'
pic_url = 'http://wxmaps.org/cgi-bin/draw_meteogram'
header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'wxmaps.org',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}
headers = {
        'Accept': '*/*',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'Content-Length': '96',
        'Content-Type': 'text/plain;charset=UTF-8',
        'Host': 'wxmaps.org',
        'Origin': 'http://wxmaps.org',
        'Referer': 'http://wxmaps.org/meteogram_custom.php',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}


datapay = '''
    <gaplot>,
    <field>,
    <lon>{}</lon>,
    <lat>{}</lat>,
    <model>0</model>,
    <unit>0</unit>,
    </field>,
    </gaplot>,
'''
lon = input('请输入经度(E)：')
lat = input('请输入纬度(N)：')
data = datapay.format(lon,lat)
res = session.get(first_url,headers = header)
time.sleep(10)
response = session.post(pic_url,data = data,headers=headers)
print(response.text)
time.sleep(10)
print('正在输出图像，请稍等！')
urllib.request.urlretrieve(response.text,'pic/' + response.text[-20:-1])
# image = requests.get(response.text)
# print(image.status_code)
# with open('pic/' + response.text[-20:-1], 'wb') as f:
#         print(image.content)
#         f.write(image.content)
print('输出完成！')
