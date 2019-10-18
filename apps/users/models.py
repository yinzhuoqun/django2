from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserProfile(AbstractUser):
    """
    用户
    """
    gender_choice = (
        ("0", "女"),
        ("1", "男"),
    )

    email = models.EmailField(verbose_name='邮箱', max_length=255, unique=True)
    phone = models.CharField(verbose_name="手机号码", max_length=50, unique=True, null=True, blank=True)
    avatar = models.URLField(verbose_name="用户头像", default="http://photo.python3.top/avatar_default.png")
    gender = models.CharField(max_length=32, choices=gender_choice, default="1", verbose_name="性别")
    time_black = models.DateTimeField(verbose_name="下次可访问时间", blank=True, null=True)
    last_ip = models.GenericIPAddressField(verbose_name="上次访问IP", default="0.0.0.0")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息列表"

    def __str__(self):
        return "%s-%s %s" % (self.username[0].upper(), self.last_name, self.first_name)


class VerifyCode(models.Model):
    """
    邮箱验证码
    """
    code = models.CharField(max_length=50, verbose_name="验证码")
    email = models.EmailField(verbose_name='邮箱', max_length=255, help_text="邮箱")
    time_create = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)  # timezone.now 不要加括号
    time_update = models.DateTimeField(verbose_name="最近获取", auto_now=True)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = "邮箱验证码列表"

    def __str__(self):
        return "%s %s" % (self.email, self.code)
