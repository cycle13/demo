import requests




session = requests.Session()
first_url = 'http://service.envicloud.cn:8082/v2/weatherhistory/ZGVTBZE0NDI5MDM0MJAZNDC=/'
first_url_day = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/dayAqi2018_county'
first_url_month = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/airreport2018_county'
first_url_year = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/airreport2018_county '
url_list = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/getCityStationDetail'
url_aqi = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/realtimeAqiOfPT '
headers = {
    'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; LIO-AN00 Build/N2G48H)'
}



def realaqi(url):
    data = {
        'time':'2020-11-02 18:00:00',
        'sort': 'asc',
        'order': 'AQI',
    }
    response = session.post(url= url,data=data,headers = headers).text
    return response

print(realaqi(url_aqi))




