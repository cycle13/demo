import requests
import time
import urllib.request
import hashlib
import wmi


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

def qipic():
    lon = input('请输入经度(E)：')
    lat = input('请输入纬度(N)：')
    data = datapay.format(lon,lat)
    res = session.get(first_url,headers = header)
    time.sleep(10)
    response = session.post(pic_url,data = data,headers=headers)
    print(response.text)
    time.sleep(10)
    print('正在输出图像，请稍等！')
    urllib.request.urlretrieve(response.text,'pic/' + lon+"_"+lat+"_"+response.text[-20:-1])
    print('输出完成！')

def readquan(xulie):
    x = open('data/data.txt','r')
    y = x.read()
    x.close()
    paw = y
    fmd5 = hashlib.md5(xulie.encode("utf-8"))
    ls = fmd5.hexdigest()[0:10]+fmd5.hexdigest()[20:30]
    fmd55 = hashlib.md5(ls.encode("utf-8"))
    ll = fmd55.hexdigest()[5:11]+fmd55.hexdigest()[15:28]
    if ll == paw:
        return 1
    else:
        return 0


def xulie():
    c = wmi.WMI()
    # # 硬盘序列号
    for physical_disk in c.Win32_DiskDrive():
        return (physical_disk.SerialNumber)
    # # CPU序列号
    # for cpu in c.Win32_Processor():
    #     print(cpu.ProcessorId.strip())
    # # 主板序列号
    # for board_id in c.Win32_BaseBoard():
    #     print(board_id.SerialNumber)
    # # mac地址
    # for mac in c.Win32_NetworkAdapter():
    #     print(mac.MACAddress)
    # # bios序列号
    # for bios_id in c.Win32_BIOS():
    #     print(bios_id.SerialNumber.strip())




if __name__ == '__main__':
    if readquan(xulie()):
        print('授权存在,请输入经纬度后按回车键等待下载！')
        qipic()
    else:
        print('该授权不存在，请输入任意键退出！')
        input()