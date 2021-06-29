#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 9:46
# @Author  : Yanjun Wang
# @Site    : 
# @File    : gif压缩.py
# @Software: PyCharm


from pygifsicle import optimize
optimize('gif/探空图.gif', "gif/optimized.gif",colors = 64)
