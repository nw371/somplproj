# Не забудьте изменить настройки в settings.py: добавить ваше новое приложение в список INSTALLED_APPS,
# обновить настройку TEMPLATES и добавить список STATICFILES_DIRS (мы уже проходили эти настройки в юнитах D1.3, D1.5).
#
# Теперь, если мы запустим наше приложение (python manage.py runserver) и попробуем перейти по адресу http://127.0.0.1:8000/products/,
#
# Оно и понятно. Мы ведь не создали шаблон, в котором мы показываем, как именно отображать наши товары.
# Создадим прямо в папке templates шаблон products.html (искренне надеемся, что у вас сохранился доработанный код со времён flatpages).
#<!--  наследуемся от шаблона default.html, который мы создавали ещё во времена flatpages -->
# {% extends 'flatpages/default.html' %}
#
# <!-- Название у нас будет proudcts -->
# {% block title %}
# Products
# {% endblock title %}
#
# <!-- В контенте на странице мы выводим все товары -->
# {% block content %}
# <h1>Все товары</h1>
# {{ products }}
# {% endblock content %}
# Теперь обновляем страницу

#Приводить все товары к вменяемому виду мы будем немного позже. Сейчас давайте взглянем, как можно вывести информацию о каком-то конкретном товаре. В дальнейшем мы сделаем так, чтобы при клике на название товара пользователь переадресовывался на страницу товара и видел все подробности о нём (наличие в магазине и полное описание).
#
# Для этого снова перейдём в файл simpleapp/views.py и немного изменим его, добавив представление для подробностей о товаре.
#
# simpleapp/views.py
#
# # from django.shortcuts import render
# from django.views.generic import ListView, DetailView  # импортируем класс получения деталей объекта
# from .models import Product
#
#
# class ProductsList(ListView):
#     model = Product
#     template_name = 'products.html'
#     context_object_name = 'products'
#
#
# # создаём представление, в котором будут детали конкретного отдельного товара
# class ProductDetail(DetailView):
#     model = Product  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
#     template_name = 'product.html'  # название шаблона будет product.html
#     context_object_name = 'product'  # название объекта. в нём будет
# В этот раз мы будем использовать DetailView. Он отличается от ListView тем, что возвращает какой-то конкретный объект, а не список всех объектов из БД. Адрес, однако, будет немного отличаться. В него надо будет добавить ID товара, которого мы хотим получить.
#
# from django.urls import path
# from .views import ProductList, ProductDetail
#
#
# urlpatterns = [
#     path('', ProductsList.as_view()),
#     path('<int:pk>', ProductDetail.as_view()),  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
# ]
# Теперь давайте добавим новый шаблон, в котором мы будем выводить отдельный товар.
#
# templates/product.html
#
# <!--  наследуемся от шаблона default.html, который мы создавали ещё во времена flatpages -->
# {% extends 'flatpages/default.html' %}
#
# <!-- Название у нас будет proudcts -->
# {% block title %}
# Products
# {% endblock title %}
#
# <!-- В контенте на странице мы выводим сам товар, ID которого было передано в адрес -->
# {% block content %}
# <h1>{{ product }}</h1>
# {% endblock content %}
# Теперь по адресу products/<id товара> мы можем получить какой-то отдельный товар и информацию о нём. Давайте это проверим. Перейдём, например, по адресу http://localhost:8000/products/1.