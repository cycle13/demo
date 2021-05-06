import requests
import json
import spidersss


session = requests.Session()

headers = {
    'Host': 'wxcharts.com',
    'Remote Address': '135.125.6.123:443',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
first_url= 'https://wxcharts.com/php/get_profile.php?lat=51.50&lon=0.00&database=00&model=gfs_profile'

res = session.get(first_url,headers=headers,verify=False).text
res = json.loads(res)
spidersss.save_to_excel(res)

