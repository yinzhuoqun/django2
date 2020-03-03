from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt

from .forms import *


# Create your views here.


def root(request):
    # with open("baidu.txt", "r") as f:
    #     f = f.readline()

    # 或者把验证文件的内容写在变量直接返回
    f = "91ad9b349b0e810a2727exxxxxxxxxxxx"

    return HttpResponse(f)


def get_csrf_token(request):
    return JsonResponse({'token': get_token(request)})


@csrf_exempt
def test_csrf(request):
    if request.method == "POST" and request.POST:
        # print(request.headers)
        name = request.POST.get("name", None)
        password = request.POST.get("password", None)
        print("xxx", request.POST.get("csrf"))
        return HttpResponse(name + password)
    return render(request, "csrf_test.html", locals())


def test_add_article(request):
    if request.method == "POST" and request.post:
        form = ArticleAdminForm
    else:
        form = ArticleAdminForm

    req = request
    return render(request, "article_add.html", locals())


def add_info(request):
    pre_page_url = request.GET.get("page", "/")
    if request.method == "POST" and request.POST:
        print(request.POST)
        form = AddInfoForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(pre_page_url)
    else:
        form = AddInfoForm
    return render(request, "add_info.html", locals())
