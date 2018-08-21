from ..models import Post
from django import template
from django.db.models.aggregates import Count
from ..models import Post, Category


register = template.Library()


# 最新文章模板标签
@register.simple_tag
def get_recent_posts(num=5):
    return Post.object.all().order_by('-created_time')[:num]


# 归档模板标签
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    # 记得在顶部引入 count 函数
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

