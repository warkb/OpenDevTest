# Generated by Django 3.0.7 on 2020-06-07 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_auto_20200607_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='published_date',
            new_name='published_year',
        ),
    ]
