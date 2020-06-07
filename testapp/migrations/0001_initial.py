# Generated by Django 3.0.7 on 2020-06-07 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('published_date', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('fathername', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('reader_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Reader')),
            ],
        ),
        migrations.CreateModel(
            name='BookTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=200)),
                ('book_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Book')),
            ],
        ),
        migrations.CreateModel(
            name='BookOrdered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('return_mark', models.BooleanField()),
                ('book_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Book')),
                ('order_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Order')),
            ],
        ),
    ]