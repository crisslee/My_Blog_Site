# coding : utf-8
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Category(models.Model):
    """
    Django要求模型必须继承models.Model类。
    Category 只需要一个分类名name就可以了
    CharField 指定分类名name 的数据类型，CharField是字符型。
    CharField 的max_lengthcabs参数指定其最大长度，超过这个长度的分类名就不能存入数据库

    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=70)

    body = models.TextField()

    created_time = models.DateTimeField()

    modified_time = models.DateTimeField()

    #文章摘要，可以没有摘要
    excertpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    #自定义get_absolute_url方法

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']