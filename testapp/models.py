from django.db import models

class Book(models.Model):
    """
    Книга
    """
    author = models.CharField(max_length=200)    # Автор
    title = models.CharField(max_length=200)    # Название
    publisher = models.CharField(max_length=200)    # Издательство
    published_date = models.IntegerField() # год издания
    price = models.IntegerField()  # цена

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
    """
    читатель
    """
    name = models.CharField(max_length=200) # имя
    surname = models.CharField(max_length=200) # фамилия
    fathername = models.CharField(max_length=200) # Отчество
    phone = models.CharField(max_length=200) # телефон