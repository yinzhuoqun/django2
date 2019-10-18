from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def root(request):
    # with open("baidu.txt", "r") as f:
    #     f = f.readline()

    # 或者把验证文件的内容写在变量直接返回
    f = "91ad9b349b0e810a2727exxxxxxxxxxxx"

    return HttpResponse(f)
