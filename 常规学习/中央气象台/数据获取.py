import requests
from lxml import etree


session = requests.Session()
first_url = 'http://www.nmc.cn/publish/observations/environmental.html'
fog_url = 'http://www.nmc.cn/publish/fog.html'
haze_url = 'http://www.nmc.cn/publish/haze.html'
dust_url = 'http://www.nmc.cn/publish/severeweather/dust.html'
air_pollution_url = ['http://www.nmc.cn/publish/environment/air_pollution-24.html','http://www.nmc.cn/publish/environment/air_pollution-48.html','http://www.nmc.cn/publish/environment/air_pollution-72.html',]

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}