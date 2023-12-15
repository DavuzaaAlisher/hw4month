"""
urls.py - Файл маршрутизации Django-проекта.

admin.site.urls - URL-адреса административного сайта.

path - функция для создания маршрута.
Принимает 2 аргумента:
1) Путь (строка)
2) Обработчик (функция, которая будет обрабатывать запрос)
"""
from django.contrib import admin
from django.urls import path

from post.views import hello_view, goodby_user, current_data


urlpatterns = [
    path('admin/', admin.site.urls),
    path('goodby/', goodby_user),
    path('hello/', hello_view),
    path('current_date/', current_data),
]