from ..models import Post, Category
from django import template

register = template.Library()

@register.simple_tag
#设置最近文章的模板标签
def get_recent_posts(num = 5):
    return Post.objects.all().order_by ('-created_time')[:num]

@register.simple_tag
#设置归档模板标签，其中dates函数三个变量分别为，文档创建时间，归档精度，返回列表顺序
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
#设置分类模板标签
def get_catrgories():
    return Category.objects.all()
