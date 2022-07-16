from random import choices
from django.db import models


class Manufacturer(models.Model):
    Manufacturers = (
        ('AMD', 'AMD'),
        ('Aorus', 'Aorus'),
        ('Asus', 'Asus'),
        ('Colorful', 'Colorful'),
        ('Cooler Master', 'Cooler Master'),
        ('Corsair', 'Corsair'),
        ('Crucial', 'Crucial'),
        ('EVGA', 'EVGA'),
        ('Gigabyte', 'Gigabyte'),
        ('Gskill', 'Gskill'),
        ('Intel', 'Intel'),
        ('Lian Li', 'Lian Li'),
        ('MSI', 'MSI'),
        ('Noctua', 'Noctua'),
        ('Nvidia', 'Nvidia'),
        ('NZXT', 'NZXT'),
        ('PNY', 'PNY'),
        ('PowerColor', 'PowerColor'),
        ('Razer', 'Razer'),
        ('Sapphire', 'Sapphire'),
        ('SAMSUNG', 'SAMSUNG'),
        ('TeamGroup', 'TeamGroup'),
        ('Thermaltake', 'Thermaltake'),
        ('Vcolor', 'Vcolor'),
        ('XFX', 'XFX'),
        ('XPG', 'XPG'),
        ('Zotac', 'Zotac'),
    )
    Id = models.CharField(primary_key=True, null=False, blank=False)

    Parent = models.CharField(choices=Manufacturers, max_length=20, null=True, blank=True, help_text='If a Graphics card is a "XFX Radeon 6600XT" for example, \
    XFX goes into the Name field, and AMD goes into the Parent field')

    Name = models.CharField(choices=Manufacturers, max_length=20, null=True, blank=True, help_text='If a Graphics card is a "XFX Radeon 6600XT" for example, \
    XFX goes into the Name field, and AMD goes into the Parent field')

    CPUs = models.BooleanField(verbose_name='Manufactures CPU')
    GPUs = models.BooleanField(verbose_name='Manufactures GPU')
    Motherboards = models.BooleanField(
        verbose_name='Manufactures Motherboards')
    RAM = models.BooleanField(verbose_name='Manufactures RAM')
    PSU = models.BooleanField(verbose_name='Manufactures PSU')
    Case = models.BooleanField(verbose_name='Manufactures Cases')
    Cooler = models.BooleanField(verbose_name='Manufactures Coolers')


class CPU_Links(models.Model):
    Id = models.ForeignKey(
        'CPU', on_delete=models.CASCADE, null=False, blank=False)
    Amazon_URL = models.URLField()
    Newegg_URL = models.URLField()
    BestBuy_URL = models.URLField()
    pass


class CPU(models.Model):
    Sockets = (
        ('AM4', 'AM4'),
        ('LGA', 'LGA'),
        ('LGA', 'LGA'),
        ('LGA', 'LGA'),
        ('LGA', 'LGA'),
        ('LGA', 'LGA'),
    )
    Id = models.CharField(primary_key=True, null=False, blank=False)
    Manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    Model_Name = models.CharField()
    Cores = models.PositiveIntegerField()
    Threads = models.PositiveIntegerField()
    Speed = models.FloatField()
    Socket = models.CharField(choices=Sockets, max_length=10)
    Power_Consumption = models.PositiveIntegerField()
    Previous_Price = models.FloatField()
    Current_Price = models.FloatField()
    Links = models.ForeignKey('CPU_Links', on_delete=models.PROTECT)
    Lowest_Price_Link = models.URLField()
    pass


class Cooler_Links(models.Model):
    Id = models.ForeignKey(
        'Cooler', on_delete=models.CASCADE, null=False, blank=False)
    Amazon_URL = models.URLField()
    Newegg_URL = models.URLField()
    BestBuy_URL = models.URLField()
    pass


class Cooler(models.Model):

    pass


class GPU_Links(models.Model):
    Id = models.ForeignKey(
        'GPU', on_delete=models.CASCADE, null=False, blank=False)
    Amazon_URL = models.URLField()
    Newegg_URL = models.URLField()
    BestBuy_URL = models.URLField()
    pass


class GPU(models.Model):
    pass


class Motherboard_Links(models.Model):
    Id = models.ForeignKey(
        'Motherboard', on_delete=models.CASCADE, null=False, blank=False)
    Amazon_URL = models.URLField()
    Newegg_URL = models.URLField()
    BestBuy_URL = models.URLField()
    pass


class Motherboard(models.Model):
    pass


class RAM_Links(models.Model):
    Id = models.ForeignKey(
        'RAM', on_delete=models.CASCADE, null=False, blank=False)
    Amazon_URL = models.URLField()
    Newegg_URL = models.URLField()
    BestBuy_URL = models.URLField()
    pass


class RAM(models.Model):
    pass


class PSU_Links(models.Model):
    Id = models.ForeignKey(
        'PSU', on_delete=models.CASCADE, null=False, blank=False)
    Amazon_URL = models.URLField()
    Newegg_URL = models.URLField()
    BestBuy_URL = models.URLField()
    pass


class PSU(models.Model):
    pass


class Case_Links(models.Model):
    Id = models.ForeignKey(
        'Case', on_delete=models.CASCADE, null=False, blank=False)
    Amazon_URL = models.URLField()
    Newegg_URL = models.URLField()
    BestBuy_URL = models.URLField()
    pass


class Case(models.Model):
    pass
