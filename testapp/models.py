from django.db import models

class Book(models.Model):
    """
    Код книги
    Автор
    Название
    Издательство
    Год издания
    Стоимость
    """
    pass

class BookOrdered(models.Model):
    # заказанные книги
    """
    Код заказа
    Код книги
    Отметка о возврате
    """
    pass
class BookTheme(models.Model):
    # теметика книги
    """
    Код
    Код книги
    Тема
    """
    pass

class Order(models.Model):
    # заказы
    """
    Код заказа
    Читатель
    Дата заказа
    """
    pass

class Reader(models.Model):
    # читатель
    """
    код читателя
    Фамилия
    Имя
    Отчество
    Телефон
    """
    pass