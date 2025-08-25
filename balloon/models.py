from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя клиента")
    phone = models.CharField(max_length=10, unique=True, verbose_name="Номер телефона")
    firm = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название фирмы')

    def __repr__(self):
        return f'<Client: {self.name}, phone: {self.phone}>'

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class BalloonType(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Наименование типа баллона')

    def __repr__(self):
        return f'<BalloonType: {self.name}>'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип баллона'
        verbose_name_plural = 'Тип баллонов'


class Balloon(models.Model):
    class StatusChoices(models.TextChoices):
        ACCEPTED_EMPTY = 'EMPTY', 'Принят пустой'
        AT_REFUELING = 'AT-REFUELING', 'Отправлен на заправку'
        ACCEPTED_FULL = 'ACCEPTED-FULL', 'Принят полный'
        AT_OWNER = 'AT-OWNER', 'У владельца'

    number = models.IntegerField(verbose_name='Номер баллона')
    type = models.ForeignKey(BalloonType, on_delete=models.CASCADE, verbose_name='Тип баллона')
    photo = models.ImageField(upload_to='media/balloon', null=True, blank=True)
    produced_at = models.DateField(verbose_name='Дата производства баллона')
    volume = models.IntegerField(verbose_name='обьем баллона')
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Владелец баллона')
    status = models.CharField(max_length=14,
                              choices=StatusChoices.choices,
                              default=StatusChoices.ACCEPTED_EMPTY,
                              verbose_name='Статус'
                              )

    def get_status_name(self):
        return dict(self.StatusChoices.choices)[self.status]

    def __str__(self):
        return f'<Balloon: {self.number}>'

    class Meta:
        verbose_name = 'Баллон'
        verbose_name_plural = 'Баллоны'
