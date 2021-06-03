#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/6 0:15
# @Author  : Ryu
# @Site    : 
# @File    : mytags.py
# @Software: PyCharm

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.inclusion_tag('pagenavi.html')
def pagenavi(num):
    return {'num':range(1,num+1)}


