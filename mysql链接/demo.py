#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/19 15:08
# @Author  : Yanjun Wang
# @Site    : 
# @File    : demo.py
# @Software: PyCharm

import pymysql
# 打开数据库连接
db = pymysql.connect(host="localhost", user="root",password='',database='financial',charset='utf8mb4')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
sql = "select * from cash"
cursor.execute(sql)
results = cursor.fetchall()
for row in results :
    id = row[7]
    idd = row[9]
    print(float(id)*float(idd))
# # 使用 execute() 方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
# print("Database version : %s " % data)
# 关闭数据库连接
db.close()
