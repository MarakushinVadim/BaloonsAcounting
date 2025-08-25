from django.db import models

from balloon.models import BalloonType, Client


class Rent(models.Model):
    type = models.ForeignKey(BalloonType, on_delete=models.CASCADE, verbose_name='Тип баллона')
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    count = models.IntegerField(verbose_name='Количество')
    volume = models.IntegerField(verbose_name='Обьем')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания', null=True, blank=True)

    class Meta:
        verbose_name = 'Аренда'
        verbose_name_plural = 'Аренда'