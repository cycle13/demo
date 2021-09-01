#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/12 16:15
# @Author  : Yanjun Wang
# @Site    : 
# @File    : manage.py.py
# @Software: PyCharm

# -*- coding: utf-8 -*-

import sys
import os
import multiprocessing

path_of_current_file = os.path.abspath(__file__)
path_of_current_dir = os.path.split(path_of_current_file)[0]

_file_name = os.path.basename(__file__)

sys.path.insert(0, path_of_current_dir)

worker_class = 'sync'  # sync,eventlet,gevent,tornado,gthread,giohttp
#workers = multiprocessing.cpu_count() * 2 + 1
workers = 10
threads = multiprocessing.cpu_count() * 4
worker_connections = 1000  # 最大客户端并发数量，默认情况下这个值为1000

max_requests = 2000  # 处理多少次请求后，服务自动重启，预防内存泄漏。默认值为0

chdir = path_of_current_dir

timeout = 30  # # 超过这么多秒后工作将被杀掉，并重新启动。一般设定为30秒
graceful_timeout = 30  # 默认情况下，这个值为30，接收到重启信号后仍执行多少秒才被强行杀死

loglevel = 'info'  # 错误日志的级别，输出error_log的颗粒度(debug、info、warning、error、critical)

reload = True
debug = False

bind = "%s:%s" % ("0.0.0.0", 2088)
pidfile = '%s/run/%s.pid' % (path_of_current_dir, _file_name)
errorlog = '%s/logs/%s_error.log' % (path_of_current_dir, _file_name)
accesslog = '%s/logs/%s_access.log' % (path_of_current_dir, _file_name)
