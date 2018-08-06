#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
名称：
日期：2018/7/13 19:54
@author: Tim.Wells

服务概述：

"""
def hanoi(x, a, b, c):  # 所有的盘子从 a 移到 c

    if x > 0:
        hanoi(x-1, a, c, b)  # step1：除了下面最大的，剩余的盘子 从 a 移到 b
        print('%s->%s' % (a, c))  # step2:最大的盘子从 a 移到 c
        hanoi(x-1, b, a, c)  # step3: 把剩余的盘子 从 b 移到 c

hanoi(3, 'A', 'B', 'C')