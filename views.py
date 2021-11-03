"""Модуль, содержащий контроллеры веб-приложения"""
from simba_framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html')

class Pizza:
    def __call__(self, request):
        return '200 OK', render('pizza.html')

class Foods:
    def __call__(self, request):
        return '200 OK', render('foods.html')

class Drinks:
    def __call__(self, request):
        return '200 OK', render('drinks.html')

class Contacts:
    def __call__(self, request):
        return '200 OK', render('contacts.html')

