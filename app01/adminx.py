# _*_ coding: utf-8 _*_
__author__ = 'wloq'
__date__ = '2019/6/9 15:53'
#在xadmin中关联注册表

import xadmin
from .models import Duanzi

class DuanziAdmin(object):
    list_display = ['author','title','content','add_time']#在xadmin中要显示的字段
    search_fields = ['author','title','content','add_time']#后台在哪些字段中搜索
    list_filter = ['author','title','content','add_time']#后台xadmin中在字段中过滤

xadmin.site.register(Duanzi,DuanziAdmin)

