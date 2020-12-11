import requests
from lxml import etree


session = requests.Session()
first_url = 'http://www.nmc.cn/publish/observations/environmental.html'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}

def real(url):
    response = session.get(url= url,headers = headers)
    response.encoding = "utf-8"
    res = response.text
    html = etree.HTML(res)
    title = html.xpath('//div[@class="writing"]/div')
    ret = html.xpath('//div[@class="writing"]/p')
    image = html.xpath('//div[@class="writing"]/div/img/@src')
    text_name = title+ret
    for i in text_name:
        if i.text != None:
            print(i.text)

    for i in image:
        if i != None:
            print(i)
    # print(ret)



# print(real(url_fog))
real(first_url)

