#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 15:52
# @Author  : Yanjun Wang
# @Site    : 
# @File    : demo1.py
# @Software: PyCharm

from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer('mars')
server.retrieve({
    "class": "od",
    "dataset": "interim",
    "date": "2019-05-10/to/2019-05-21",
    'time' : "00/06/12/18",
    "grid": "0.75/0.75",
    "levelist": "1/2/3/5/7/10/20/30/50/70/100/125/150/175/200/225/250/300/350/400/450/500/550/600/650/700/750/775/800/825/850/875/900/925/950/975/1000",
    "levtype": "sfc",
    "param": "134.128/151.128/165.128/166.128/167.128/168.128",
    "step": "3",
    "stream": "oper",
    'area':'55/75/15/135',
    "type": "an",
    'format' : "netcdf",
    "target": "output1.nc",
})
