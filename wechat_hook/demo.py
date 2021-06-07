# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import wechat
import county_aqi
import taiyuan
import os
import json
import time
from wechat import WeChatManager, MessageType

wechat_manager = WeChatManager(libs_path='../../libs')


# 这里测试函数回调
@wechat.CONNECT_CALLBACK(in_class=False)
def on_connect(client_id):
    print('[on_connect] client_id: {0}'.format(client_id))


@wechat.RECV_CALLBACK(in_class=True)
def on_recv(client_id, message_type, message_data):
    print('[on_recv] client_id: {0}, message_type: {1}, message:{2}'.format(client_id,message_type, json.dumps(message_data)))



@wechat.RECV_CALLBACK(in_class=False)
def on_message(client_id, message_type, message_data):
    if message_data["from_wxid"] != 'wxid_pjni8giv9pg222':
        print(message_data["msg"])
        if message_data["msg"] == '环境公报':
            # wechat_manager.send_text(client_id, message_data["from_wxid"], '该消息通过微信机器人接口发送')
            county_aqi.real()
            dir_list = os.listdir(r'D:\Program Files\pycharm\wechat_hook\county_image')
            for i in dir_list:
                path = r"D:\Program Files\pycharm\wechat_hook\county_image"+'\\'+i
                wechat_manager.send_image(client_id, message_data["from_wxid"], path)
                print(message_data)
            time.sleep(10)
            del_files(r'D:\Program Files\pycharm\wechat_hook\county_image')
        elif message_data["msg"] in ["金胜","坞城","南寨","桃园","巨轮","小店","尖草坪","上兰","晋源","西山","老军营"] :
            l = taiyuan.station(message_data["msg"])
            wechat_manager.send_text(client_id, message_data["from_wxid"], '{}站点SO2浓度：{}μg/m3,NO2浓度:{}μg/m3,PM10浓度：{}μg/m3,CO浓度：{}mg/m3,O3浓度：{}μg/m3,PM2.5浓度：{}μg/m3,AQI值：{}，空气质量等级：{}'.format(message_data["msg"],l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7]))
    else:
        return


@wechat.CLOSE_CALLBACK(in_class=False)
def on_close(client_id):
    print('[on_close] client_id: {0}'.format(client_id))


# 这里测试类回调， 函数回调与类回调可以混合使用
class LoginTipBot(wechat.CallbackHandler):

    @wechat.RECV_CALLBACK(in_class=True)
    def on_message(self, client_id, message_type, message_data):
        # 判断登录成功后，就向文件助手发条消息
        if message_type == MessageType.MT_USER_LOGIN:
            time.sleep(2)
            wechat_manager.send_text(client_id, 'filehelper', '该消息通过微信机器人接口发送')
            
            wechat_manager.send_link(client_id, 
            'filehelper', 
            '公众号',
            '晴颸 浮阳',
            'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzI1NDQ2NTMwNw==&scene=124#wechat_redirect',
            'https://mp.weixin.qq.com/s/mxVsELHVnqFePeu_5DFy2Q)')
            wechat_manager.get_friends(client_id)
            wechat_manager.send_file(client_id, 'filehelper', r'E:\2.0app\app问题.docx')


# 每发完一次删除文件夹下的图片
def del_files(path_file):
    ls = os.listdir(path_file)
    for i in ls:
        f_path = os.path.join(path_file, i)
        # 判断是否是一个目录,若是,则递归删除
        if os.path.isdir(f_path):
            del_files(f_path)
        else:
            os.remove(f_path)

if __name__ == "__main__":
    bot = LoginTipBot()

    # 添加回调实例对象
    wechat_manager.add_callback_handler(bot)
    wechat_manager.manager_wechat(smart=True)

    # 阻塞主线程
    while True:
        time.sleep(2)
