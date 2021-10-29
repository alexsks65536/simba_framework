"""Модуль, содержащий контроллеры веб-приложения"""
from simba_framework.templator import render


class Index:
    def __call__(self):
        return '200 OK', render('index.html')

class Style:
    def __call__(self):
        return '200 OK', render('style.css')

class Pizza:
    def __call__(self):
        return '200 OK', render('pizza.html')

class Foods:
    def __call__(self):
        return '200 OK', render('foods.html')

class Drinks:
    def __call__(self):
        return '200 OK', render('drinks.html')

class Pizza_logo:
    def __call__(self):
        return '200 OK', render('Pizza_logo.jpg')
