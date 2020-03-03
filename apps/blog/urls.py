#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: yinzhuoqun
@site: http://xieboke.net/
@email: yin@zhuoqun.info
@time: 2019/12/26 15:40
"""

from django.urls import path, re_path, include
from . import views

app_name = "apps.blog"

urlpatterns = [
    path("get_token", views.get_csrf_token),
    path("test_csrf", views.test_csrf),
    path("article_add", views.test_add_article),
    path("add_info", views.add_info, name="add_info"),
]
