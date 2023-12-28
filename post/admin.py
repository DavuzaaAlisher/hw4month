'''
admin.py - Файл настроек административного сайта.
'''

from django.contrib import admin

from post.models import Product, Category, Hashtag


admin.site.register(Product)

admin.site.register(Category)

admin.site.register(Hashtag)


