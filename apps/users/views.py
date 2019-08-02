from django.shortcuts import render
# from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
# from .models import UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.

# 让用户可以用邮箱登录
# setting 里要有对应的配置 AUTHENTICATION_BACKENDS
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None
