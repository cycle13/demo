import re
import json
import execjs
import requests
import warnings
from lxml import etree

warnings.filterwarnings('ignore')


class GetWeather(object):
    def __init__(self):
        self.url = 'https://www.aqistudy.cn/html/city_detail.php?v=1.10'
        self.api = 'https://www.aqistudy.cn'
        self.headers = {
            'Host': 'www.aqistudy.cn',
            'Origin': 'https://www.aqistudy.cn',
            'Referer': 'https://www.aqistudy.cn/html/city_detail.php?v=1.10',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; ZTE BA520 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.77 Mobile Safari/537.36',
        }
        self.req_url = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
        self.js_code = None
        self.js_ctx = None
        self.encrypt_func = None
        self.encrypt_param = None
        self.decode_func = None

    def init_js_code(self):
        try:
            response = requests.get(url=self.url, headers=self.headers, verify=False)
            html = etree.HTML(response.text)
            js_path = html.xpath('/html/body/script[2]/@src')[0]
            # print(self.api + js_path[2:])

            response = requests.get(url=self.api + js_path[2:], headers=self.headers, verify=False)
            # print(response.text)
            # 加密参数的函数名
            pat_f = r'var param = (.*)\(.*\)'
            self.encrypt_func = re.findall(pat_f, response.text)[0]
            # print(func_name)
            # post提交数据的参数名
            pat_p = r'(?<=\{).+(?=\})'
            print(response.text)
            self.encrypt_param = re.search(pat_p, response.text)[0].split(':')[0].strip()
            # print(param_name)
            # deocde函数
            pat_d = r'data = (.*)\(.*\)'
            self.decode_func = re.findall(pat_d, response.text)[-1]
            # print(func_decode)

            '''
            组合js代码
            '''
            with open('gogo.js', 'r', encoding='utf-8') as fp:
                self.js_code = fp.read()
            self.js_code += response.text
            self.js_ctx = execjs.compile(self.js_code)
        except Exception as e:
            print(e)

    def get_weather_data(self, method, obj):
        param = {
            self.encrypt_param: self.js_ctx.call(self.encrypt_func, method, obj)
        }
        print(param)
        response = requests.post(url=self.req_url, headers=self.headers, data=param, verify=False)
        return self.js_ctx.call(self.decode_func, response.text)

    def run(self, method, obj, months: list):
        self.init_js_code()
        for mon in months:
            if mon[0] == '2020-08-01':
                obj.update({"startTime": f"{mon[0]} 00:00:00"})
                obj.update({"endTime": f"{mon[1]} 00:00:00"})
                js_data = self.get_weather_data(method, obj)
                # with open('urumqi_weather_2020.json', 'a', encoding = 'utf-8') as wf:
                #     wf.write(js_data + '\n')
                js_data = json.loads(js_data)['result']['data']['rows']
                max_per_month = max(js_data, key=lambda x: float(x['temp']))['temp']
                min_per_month = min(js_data, key=lambda x: float(x['temp']))['temp']
                ave_per_month = sum([float(i['temp']) for i in js_data])
                print([max_per_month, min_per_month, round(ave_per_month / len(js_data), 1)])


if __name__ == '__main__':
    obj = {"city": "乌鲁木齐", "type": "DAY", "startTime": "2020-08-01 00:00:00", "endTime": "2020-08-14 00:00:00"}
    # 'GETCITYWEATHER'获取天气数据如温度、湿度、风力大小
    # 'GETDETAIL'获取 pm2.5、co、so2...
    method = "GETCITYWEATHER"
    ll = map(lambda m, d: "2020" + '-' + "%02d" % m + '-' + "%02d" % d, [_ for _ in range(1, 9)],
             [31, 28, 31, 30, 31, 30, 31, 18])
    months = map(lambda x, y: ("2020" + '-' + "%02d" % x + '-' + "01", y), [_ for _ in range(1, 9)],
                 [_ for _ in list(ll)])
    d = GetWeather()
    d.run(method, obj, months)