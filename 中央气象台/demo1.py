import win32api
import win32con
import win32gui
import pandas as pd
import time
import win32clipboard as w
import requests
import json
from win32com.client import Dispatch, DispatchEx
from PIL import ImageGrab, Image
import uuid
import xlwt
import openpyxl
import openpyxl.styles
from openpyxl.styles import PatternFill



session = requests.Session()
first_url = 'http://www.nmc.cn/'
url_fog = 'http://www.nmc.cn/publish/fog.html'
url_haze = 'http://www.nmc.cn/publish/haze.html'
url_dust = 'http://www.nmc.cn/publish/severeweather/dust.html'
url_air_pollution = 'http://www.nmc.cn/publish/environment/air_pollution-24.html'
url_environmental = 'http://www.nmc.cn/publish/observations/environmental.html'
url_National_environment = 'http://www.nmc.cn/publish/environment/National-Bulletin-atmospheric-environment.html'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}

def real(url):
    response = session.get(url= url,headers = headers).text
    return response



# print(real(url_fog))
print(real(url_air_pollution))

