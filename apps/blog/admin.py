from django.contrib import admin
from django.forms import widgets
from apps.blog.models import *
from apps.blog.forms import ArticleAdminForm
from django.contrib.admin import SimpleListFilter


# Register your models here.


class NodeFilter(SimpleListFilter):
    title = 'node'  # or use _('country') for translated title
    parameter_name = 'node'

    def lookups(self, request, model_admin):
        # 查出 node 的 id 和 name 值 用来显示在网页上的筛选条件
        nodes = Node.objects.all()
        return [(node.id, node.name + "-自定义") for node in nodes]

    def queryset(self, request, queryset):
        if self.value():
            # 筛选条件有值时, 查询对应的 node 的文章，用 title 正排序
            return queryset.filter(node__id=self.value()).order_by("title")
        else:
            # 筛选条件没有值时，全部的时候是没有值的
            return queryset


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
    change_list_template = "friend_url_add_at_article.html"

    form = ArticleAdminForm  # 指定了表单，就不要再用 formfield_overrides 了

    list_display = ['id', 'thumb_shouw', 'title', 'node', 'num_views', 'show_status', 'slug', 'user', 'time_create']
    list_display_links = ['id', 'thumb_shouw', 'title', 'node', 'num_views', 'user']
    list_filter = ['id', 'source__name', NodeFilter]
    search_fields = ['title_short', 'user', 'content']
    list_editable = ["show_status", ]
    # style_fields = {"content": "ueditor"}
    readonly_fields = ('slug',)
    show_detail_fields = ['show_status', ]

    # 重写 字段类型 的 widget, attrs 属性可以设置前端样式
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
