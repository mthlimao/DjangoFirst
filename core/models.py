from django.db import models


class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    inventory = models.IntegerField('Quantidade em Estoque')

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField('Nome', max_length=100)
    surname = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-Mail', max_length=100)

    def __str__(self):
        return f"{self.name} {self.surname}"
