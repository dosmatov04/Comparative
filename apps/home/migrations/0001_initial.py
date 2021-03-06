# Generated by Django 3.2.9 on 2021-11-10 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('logo', models.ImageField(upload_to='banner', verbose_name='logo')),
                ('keyword', models.CharField(max_length=255, verbose_name='Ключевые слова')),
                ('phone', models.CharField(max_length=20, verbose_name='телефон')),
                ('time_work', models.CharField(max_length=255, verbose_name='время работы')),
                ('day_work', models.CharField(max_length=255, verbose_name='дни работы')),
                ('email', models.CharField(max_length=255, verbose_name='email')),
                ('address', models.CharField(max_length=255, verbose_name='address')),
                ('facebook', models.CharField(max_length=255, verbose_name='facebook')),
                ('instagram', models.CharField(max_length=255, verbose_name='instagram')),
                ('telegram', models.CharField(max_length=255, verbose_name='telegram')),
                ('twitter', models.CharField(max_length=255, verbose_name='twitter')),
            ],
            options={
                'verbose_name_plural': 'Основные настройки',
            },
        ),
    ]
