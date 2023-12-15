'''
views.py - Файл представлений приложения.
View - это функция, которая принимает запрос и возвращает ответ.

HttpResponse - класс, который представляет собой ответ сервера.

HTTP - протокол передачи гипертекста. HyperText Transfer Protocol.
HTTPs - защищенный протокол передачи гипертекста. HyperText Transfer Protocol Secure.

Method - метод. GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD.

render - функция, которая принимает запрос, имя шаблона и словарь с данными и возвращает ответ.
'''
from django.shortcuts import render
from django.http import HttpResponse
import datetime


def goodby_user(request):
    if request.method == 'GET':  # GET - получение данных
        return HttpResponse('goodby_user')


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello!its my project')


def current_data(request):
    if request.method == 'GET':
        return HttpResponse(datetime.datetime.date())
