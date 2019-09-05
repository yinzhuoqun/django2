#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: yinzhuoqun
@site: http://zhuoqun.info/
@email: yin@zhuoqun.info
@time: 2019/9/5 15:26
"""
from django import forms
from django.forms.widgets import TextInput
from apps.blog.models import Article


class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            "title": TextInput(attrs={"style": "width:50%;", "placeholder": "请输入标题"}),
        }
