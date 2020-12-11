import requests
from lxml import etree


session = requests.Session()
first_url = 'http://www.nmc.cn/publish/observations/environmental.html'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}

def real():
    response = session.get(url= first_url,headers = headers)
    response.encoding = "utf-8"
    res = response.text
    html = etree.HTML(res)
    title = html.xpath('//div[@class="writing"]/div')
    ret = html.xpath('//div[@class="writing"]/p')
    image = html.xpath('//div[@class="writing"]/div/img/@src')
    text_name = title+ret
    text_x = []
    for i in text_name:
        if i.text != None:
            text_x.append(i.text)

    for i in range(len(image)):
        if image[i] != None:
            res = session.get(image[i],headers = headers)
            with open('county_image/' + str(i) + '.jpg', 'wb') as f:
                f.write(res.content)
    return text_x