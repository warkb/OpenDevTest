# Generated by Django 3.0.7 on 2020-06-07 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20200607_1230'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterModelOptions(
            name='bookordered',
            options={'verbose_name': 'Заказ книги', 'verbose_name_plural': 'Заказы книг'},
        ),
        migrations.AlterModelOptions(
            name='booktheme',
            options={'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='reader',
            options={'verbose_name': 'Читатель', 'verbose_name_plural': 'Читатели'},
        ),
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='Автор',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='publisher',
            new_name='Издательство',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='title',
            new_name='Название',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='price',
            new_name='год издания',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='published_date',
            new_name='цена',
        ),
        migrations.RenameField(
            model_name='bookordered',
            old_name='order_code',
            new_name='Заказ',
        ),
        migrations.RenameField(
            model_name='bookordered',
            old_name='book_code',
            new_name='Книга',
        ),
        migrations.RenameField(
            model_name='bookordered',
            old_name='return_mark',
            new_name='Отметка о возврате',
        ),
        migrations.RenameField(
            model_name='booktheme',
            old_name='theme',
            new_name='Жанр',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='date',
            new_name='Дата заказа',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='reader_code',
            new_name='Читатель',
        ),
        migrations.RenameField(
            model_name='reader',
            old_name='fathername',
            new_name='Имя',
        ),
        migrations.RenameField(
            model_name='reader',
            old_name='name',
            new_name='Отчество',
        ),
        migrations.RenameField(
            model_name='reader',
            old_name='phone',
            new_name='Телефон',
        ),
        migrations.RenameField(
            model_name='reader',
            old_name='surname',
            new_name='Фамилия',
        ),
    ]
