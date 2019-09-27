from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.utils.html import format_html
# from django.template.defaultfilters import slugify
# from ckeditor.fields import RichTextField  # 不包含上传文件
from ckeditor_uploader.fields import RichTextUploadingField  # 包含上传文件
from pyquery import PyQuery as pq  # pip install pyquery, 获取到html中的img图片地址返回
# from pypinyin import lazy_pinyin  # pip install pypinyin
from uuslug import slugify  # pip install django-uuslug

User = get_user_model()


# Create your models here.


class Source(models.Model):
    """
    文章来源
    """
    name = models.CharField(max_length=128, default="原创", unique=True, verbose_name="站点名称")
    url = models.URLField(max_length=128, blank=True, null=True, verbose_name="url")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "文章来源"
        verbose_name_plural = "文章来源列表"

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    节点类别表
    """
    name = models.CharField(max_length=128, unique=True, verbose_name="类别名称")
    slug = models.SlugField(max_length=128, unique=True, verbose_name="url标识符")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "节点类别"
        verbose_name_plural = "节点分类列表"

    def __str__(self):
        return self.name


class Node(models.Model):
    """
    节点表
    """
    name = models.CharField(max_length=128, unique=True, verbose_name="节点名称")

    # SlugField 是一个新闻术语（通常叫做短标题）。一个slug只能包含字母、数字、下划线或者是连字符，通常用来作为短标签。通常它们是用来放在地址栏的URL里的。
    # 像CharField一样，你可以指定max_length（也请参阅该部分中的有关数据库可移植性的说明和max_length）。如果没有指定
    # max_length, Django将会默认长度为50。
    # 将Field.db_index设置为True。
    # 根据某些其他值的值自动预填充SlugField通常很有用。你可以在admin中使用prepopulated_fields自动执行此操作。
    slug = models.SlugField(max_length=128, unique=True, verbose_name="url标识符")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    num_topics = models.IntegerField(default=0, verbose_name="主题数量")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name="所属类别")
    show_status = models.BooleanField(default=True, verbose_name="显示状态")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Node, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "节点"
        verbose_name_plural = "节点列表"

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    文章标签
    """
    name = models.CharField(max_length=50, unique=True, verbose_name="标签")
    slug = models.SlugField(max_length=128, unique=True, verbose_name="url标识符")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "文章标签"
        verbose_name_plural = "文章标签列表"

    def __str__(self):
        return self.name


class Article(models.Model):
    """
    主题表/文章表
    """
    title = models.CharField(max_length=128, unique=True, verbose_name="标题")
    slug = models.SlugField(max_length=128, unique=True, verbose_name="url标识符")
    content = RichTextUploadingField(verbose_name="内容", config_name='awesome_ckeditor')
    node = models.ForeignKey(Node, on_delete=models.DO_NOTHING, verbose_name="所属节点")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="user_article", verbose_name="作者")
    source = models.ForeignKey(Source, on_delete=models.DO_NOTHING, verbose_name="来源", blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name="标签", related_name="tags_article", blank=True)
    num_views = models.IntegerField(default=0, verbose_name="浏览数量")
    num_favorites = models.IntegerField(default=0, verbose_name="收藏数量")
    last_answerer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="last_answerer_article",
                                      verbose_name="最后回复者", blank=True,
                                      null=True)
    show_status = models.BooleanField(default=True, verbose_name="显示状态")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="发表时间")
    time_update = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name="更新时间")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    # 获取后台文本编辑器图文内容中图片url地址
    def get_content_img_url(self):
        temp = Article.objects.filter(pk=str(self.id)).values('content')  # values获取Article数据表中的content字段内容
        html = pq(temp[0]['content'])  # pq方法获取编辑器html内容
        # print(html, "\n", "----")
        img_path = pq(html)('img').attr('src')  # 截取html内容中的路径
        # print("pic", img_path)
        return img_path  # 返回第一张图片路径

    # 管理后台显示文章的缩略图
    def thumb_shouw(self):
        if self.get_content_img_url():
            return format_html(
                '<span><img src="{}"/>{}</span>', self.get_content_img_url(), "这里是缩略图")
        else:
            return format_html('<span style="color:{}">{}</span>', "red", "暂无缩略图")

    thumb_shouw.short_description = format_html('<span class="text">缩略图</span>')   # 新字段的显示的名称，相当于 verbose_name
    thumb_shouw.admin_order_field = "-time_update"  # 指定排序方式，更新时间倒序排列

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章列表"

    def __str__(self):
        title_short = self.title if len(self.title) < 15 else self.title[:12] + '...'
        return "%s %s %s" % (self.id, self.user, title_short)


class FriendsURL(models.Model):
    friend_name = models.CharField(max_length=50, unique=True, verbose_name="用户名称")
    friend_image = models.ImageField(max_length=8 * 1024 * 1024 * 5, upload_to="friends", verbose_name="用户头像")
    site_name = models.CharField(max_length=50, unique=True, verbose_name="网站名称")
    site_link = models.URLField(max_length=256, blank=True, null=True, verbose_name="网站链接")
    show_status = models.BooleanField(default=True, verbose_name="显示状态")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    time_update = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "友情链接"
        verbose_name_plural = "友情链接列表"

    def __str__(self):
        return self.friend_name
