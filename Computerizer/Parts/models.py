from random import choices
from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    Manufacturers = [
        ('MSI', 'MSI'),
        ('Asus', 'Asus')
    ]
    Name = models.CharField()
    Range = models.CharField()


class CPU_Links(models.Model):
    Id = models.ForeignKey('CPU')
    Amazon_URL = models.TextField()
    Newegg_URL = models.TextField()
    BestBuy_URL = models.TextField()
    pass


class CPU(models.Model):
    Id = models.CharField()
    Manufacturer = models.ForeignKey('Manufacturer')
    Model_Name = models.CharField()
    Cores = models.PositiveIntegerField()
    Threads = models.PositiveIntegerField()
    Speed = models.FloatField()
    Socket = models.CharField()
    Power_Consumption = models.PositiveIntegerField()
    Previous_Price = models.FloatField()
    Current_Price = models.FloatField()
    Links = models.ForeignKey('CPU_Links')
    Lowest_Price_Link = models.ForeignKey('Links')
    pass


Amazon
Newegg
Bestbuy


class GPU_Links(models.Model):
    Id = models.ForeignKey('GPU')
    Amazon_URL = models.TextField()
    Newegg_URL = models.TextField()
    BestBuy_URL = models.TextField()
    pass


class GPU(models.Model):
    pass


class Motherboard_Links(models.Model):
    Id = models.ForeignKey('Motherboard')
    Amazon_URL = models.TextField()
    Newegg_URL = models.TextField()
    BestBuy_URL = models.TextField()
    pass


class Motherboard(models.Model):
    pass


class RAM_Links(models.Model):
    Id = models.ForeignKey('RAM')
    Amazon_URL = models.TextField()
    Newegg_URL = models.TextField()
    BestBuy_URL = models.TextField()
    pass


class RAM(models.Model):
    pass


class PSU_Links(models.Model):
    Id = models.ForeignKey('PSU')
    Amazon_URL = models.TextField()
    Newegg_URL = models.TextField()
    BestBuy_URL = models.TextField()
    pass


class PSU(models.Model):
    pass


class Case_Links(models.Model):
    Id = models.ForeignKey('Case')
    Amazon_URL = models.TextField()
    Newegg_URL = models.TextField()
    BestBuy_URL = models.TextField()
    pass


class Case(models.Model):
    pass
