# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import wechat
import json
import time
from wechat import WeChatManager, MessageType

wechat_manager = WeChatManager(libs_path='../../libs')


# 这里测试函数回调
@wechat.CONNECT_CALLBACK(in_class=False)
def on_connect(client_id):
    print('[on_connect] client_id: {0}'.format(client_id))


@wechat.RECV_CALLBACK(in_class=False)
def on_recv(client_id, message_type, message_data):
    print('[on_recv] client_id: {0}, message_type: {1}, message:{2}'.format(client_id,
                                                                            message_type, json.dumps(message_data)))


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


if __name__ == "__main__":
    bot = LoginTipBot()

    # 添加回调实例对象
    wechat_manager.add_callback_handler(bot)
    wechat_manager.manager_wechat(smart=True)

    # 阻塞主线程
    while True:
        time.sleep(0.5)
