from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=15, verbose_name="Телефон", blank=True, null=True)
    message = models.TextField(verbose_name="Сообщение")

    def __str__(self):
        return self.name
