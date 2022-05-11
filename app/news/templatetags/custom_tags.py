from django import template
from news.models import Blog


register = template.Library()


# def get_liked_users(following, likes):
#     return set(following).intersection(set(likes))