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
    test_field = forms.CharField(label="测试字段", help_text="请输入")

    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            "title": TextInput(attrs={"style": "width:45%;", "placeholder": "请输入标题"}),
        }


class AddInfoForm(forms.Form):
    select_choice = (
        ('1', '测试1'),
        ("2", "测试2"),
        ("3", "测试3"),
        ("4", "测试4"),
    )

    test_input = forms.CharField(label="测试输入框", help_text="测试输入框")
    test_select = forms.CharField(label="测试下拉框", help_text="测试多选框", initial="in",
                                  widget=forms.RadioSelect(choices=select_choice, attrs={'class': 'form-control'}))
    test_select1 = forms.CharField(label="测试下拉框1", help_text="测试多选框1",
                                   widget=forms.Select(choices=select_choice, attrs={'class': 'form-control'}))
