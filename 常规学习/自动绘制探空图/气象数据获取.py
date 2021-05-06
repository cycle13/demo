import requests
import json
import spidersss


session = requests.Session()

headers = {
    'Host': 'wxcharts.com',
    'Remote Address': '135.125.6.123:443',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
first_url= 'https://wxcharts.com/php/get_gfs.php?days=10&lat=38.00&lon=111.75&database=00'
data = {
    'days': '10',
    'lat': '38.00',
    'lon': '111.75',
    'database': '00'
}
res = session.post(first_url,headers=headers,verify=False,data=data).text
res = json.loads(res)
print(res)
spidersss.save_to_excelqi(res)
