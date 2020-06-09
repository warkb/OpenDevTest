from django.db import models

class Book(models.Model):
    """
    Книга
    """
    author = models.CharField(max_length=200)    # Автор
    title = models.CharField(max_length=200)    # Название
    publisher = models.CharField(max_length=200)    # Издательство
    published_year = models.IntegerField() # год издания
    price = models.IntegerField()  # цена
    theme_code = models.ForeignKey(
        'BookTheme', on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

class BookOrdered(models.Model):
    order_code = models.ForeignKey(
        'Order', on_delete=models.CASCADE)#Код заказа

    book_code = models.ForeignKey(
        'Book', on_delete=models.CASCADE) # Код книги
    return_mark = models.BooleanField() #Отметка о возврате
    class Meta:
        verbose_name = 'Книга в заказе'
        verbose_name_plural = 'Книги в заказе'

class BookTheme(models.Model):
    # тематика книги
    """
    Тема
    """
    theme = models.CharField(max_length=200)

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class Order(models.Model):
    """
    заказы
    """
    reader_code = models.ForeignKey(
        'Reader', on_delete=models.CASCADE) # Читатель
    date = models.DateField() # Дата заказа

    def __str__(self):
        return 'Заказ от ' + str(self.date)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Reader(models.Model):
    """
    читатель
    """
    surname = models.CharField(max_length=200) # фамилия
    name = models.CharField(max_length=200) # имя
    fathername = models.CharField(max_length=200) # Отчество
    phone = models.CharField(max_length=200) # телефон

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'