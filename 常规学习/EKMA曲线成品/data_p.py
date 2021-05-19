import requests
import time
from lxml import etree
import json

session = requests.Session()
headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Content-Length': '2484',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'www.shodor.org',
        'Origin': 'http://www.shodor.org',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://www.shodor.org/ekma//model/ozipform.html',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'

}
headers1 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'www.shodor.org',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://www.shodor.org/cgi-bin/ozip/ozip.pl',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'

}
headers2 = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'

}
fir_url = 'http://www.shodor.org/ekma//model/ozipform.html'
url = 'http://www.shodor.org/cgi-bin/ozip/ozip.pl'


def reqpost(dat,head):
    res1 = session.post(url, data=dat, headers=head)
    if res1.status_code != 200:
        reqpost(dat,head)
    return res1

def reqget(url,head):
    res1 = session.get(url,headers=head)
    if res1.status_code != 200:
        res1 = reqget(url,head)
    return res1


def data_p(name):
    with open('data_data/data2.json', encoding='utf-8') as f:
        data = json.load(f)
    session.get(fir_url,headers = headers2)
    time.sleep(10)
    print('正在对输入数据进行计算！')
    res1 = reqpost(data,headers)
    html = etree.HTML(res1.text)
    all_url = html.xpath('/html/body/li/a/@href')
    oziso_url = 'http://www.shodor.org' + all_url[1]
    time.sleep(10)
    res = reqget(oziso_url,headers1)
    txt = open('data/output.txt', 'w')
    txt.write(res.text)
    time.sleep(10)
    oziso_url = 'http://www.shodor.org'+all_url[2]
    time.sleep(10)
    print('正在导出计算结果数据！')
    res = reqget(oziso_url, headers1)
    txt = open('data/'+name+'.txt', 'w')
    txt.write(res.text)
    voc = data['basevoc']
    nox = data['basenox']
    return voc,nox