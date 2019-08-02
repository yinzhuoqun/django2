from django.contrib import admin
from apps.users.models import UserProfile
from django.utils.translation import ugettext as _
from django.contrib.auth.forms import (UserChangeForm, )
from .forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'email', 'phone', 'last_name', 'first_name', 'is_active', 'is_staff', 'is_superuser')
    list_display_links = ('username', 'email', 'phone')
    list_editable = ['is_active', 'is_staff', 'is_superuser']
    # readonly_fields = ['password', ]
    # def get_model_form(self, **kwargs):
    #     """
    #     1.把 django UserCreationForm 拷贝出来修改成自己想要的
    #     2.修改 xadmin 继承表格，改成一步骤的表单
    #     :param kwargs:
    #     :return:
    #     """
    #     if self.org_obj is None:
    #         self.form = UserCreationForm
    #     else:
    #         self.form = UserChangeForm
    #     return super(UserProfileAdmin, self).get_model_form(**kwargs)


admin.site.register(UserProfile, UserProfileAdmin)
