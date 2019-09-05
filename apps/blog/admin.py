from django.contrib import admin
from django.forms import widgets
from apps.blog.models import *
from apps.blog.forms import ArticleAdminForm


# Register your models here.


class SourceAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['id', 'name', 'url']


class CategoryAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['id', 'name', 'slug']
    readonly_fields = ('slug',)


class NodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'category', 'num_topics', 'show_status']
    list_display_links = ['id', 'name', 'slug', 'category', 'num_topics']
    list_editable = ["show_status", ]
    readonly_fields = ('slug',)


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_display_links = ['id', 'name', 'slug']
    readonly_fields = ('slug',)


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm  # 指定了表单，就不要再用 formfield_overrides 了

    list_display = ['id', 'thumb_shouw', 'title', 'node', 'num_views', 'show_status', 'slug', 'user']
    list_display_links = ['id', 'thumb_shouw', 'title', 'node', 'num_views', 'user']
    search_fields = ['title_short', 'user', 'content']
    list_editable = ["show_status", ]
    # style_fields = {"content": "ueditor"}
    readonly_fields = ('slug',)
    show_detail_fields = ['show_status', ]

    # 重写 字段类型 的 widget, attrs 属性可以设置前端数量
    # formfield_overrides = {
    #     models.IntegerField: {'widget': widgets.NumberInput(attrs={"style": "width:50em;", })},
    #     models.CharField: {'widget': widgets.TextInput(attrs={"style": "width:50%;", "placeholder": "请输入内容"})},
    # }


class FriendsURLAdmin(admin.ModelAdmin):
    list_display = ['id', 'friend_name', 'site_name', 'show_status', 'site_link']
    list_display_links = ['id', 'friend_name', 'site_name', 'site_link']
    list_editable = ["show_status", ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Node, NodeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(FriendsURL, FriendsURLAdmin)
