from django.db import models


class Setting(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    logo = models.ImageField(upload_to="banner", verbose_name="logo")
    keyword = models.CharField(verbose_name="Ключевые слова", max_length=255)
    phone = models.CharField(max_length=20, verbose_name="телефон")
    time_work = models.CharField(max_length=255, verbose_name="время работы")
    day_work = models.CharField(max_length=255, verbose_name="дни работы")
    email = models.CharField(max_length=255, verbose_name="email")
    address = models.CharField(max_length=255, verbose_name="address")

    facebook = models.CharField(max_length=255, verbose_name="facebook")
    instagram = models.CharField(max_length=255, verbose_name="instagram")
    telegram = models.CharField(max_length=255, verbose_name="telegram")
    twitter = models.CharField(max_length=255, verbose_name="twitter")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Основные настройки'
