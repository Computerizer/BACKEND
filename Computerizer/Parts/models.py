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
        ('NvIDia', 'NvIDia'),
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
    ID = models.CharField(primary_key=True, null=False, blank=False, max_length=50)

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

    def __str__(self):
        return f"{self.Name} -> ({self.Parent})"


class CPU_Links(models.Model):
    ID = models.ForeignKey('CPU', on_delete=models.CASCADE, null=False, blank=False)
    Amazon_URL = models.URLField()
    Newegg_URL = models.URLField()
    BestBuy_URL = models.URLField()
    pass

    def __str__(self):
        return f"CPU: ({self.ID})"


class CPU(models.Model):
    Sockets = (
        ('AM4', 'AM4'),
        ('LGA 1700', 'LGA 1700'),
        ('LGA 1200', 'LGA 1200')
    )
    ID                = models.CharField(primary_key=True, null=False, blank=False, max_length=6)
    Manufacturer      = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    Model_Name        = models.CharField(max_length=20)
    Cores             = models.PositiveIntegerField()
    Threads           = models.PositiveIntegerField()
    Speed             = models.FloatField()
    Socket            = models.CharField(choices=Sockets, max_length=15)
    Power_Consumption = models.PositiveIntegerField()
    Previous_Price    = models.FloatField()
    Current_Price     = models.FloatField()
    Links             = models.ForeignKey('CPU_Links', on_delete=models.PROTECT)
    Lowest_Price_Link = models.URLField()
    pass

    def __str__(self):
        return f"{self.Model_Name} ({self.ID})"


class AirCooler_Links(models.Model):
    ID = models.ForeignKey(
        'AirCooler', on_delete=models.CASCADE, null=False, blank=False)
    Amazon_URL = models.URLField()
    Newegg_URL = models.URLField()
    BestBuy_URL = models.URLField()
    pass


class AirCooler(models.Model):
    Sockets = (
        ('AM4', 'AM4'),
        ('LGA 1700', 'LGA 1700'),
        ('LGA 1200', 'LGA 1200')
    )

    Sizes = (
        ('Large', 'Large'),
        ('Average', 'Average'),
        ('Small', 'Small')
    )

    ID                = models.CharField(primary_key=True)
    Manufacturer      = models.ForeignKey('Manufacturer')
    Socket            = models.CharField(choices=Sockets, max_length=15)
    Size              = models.CharField(choices=Sizes, max_length=10)
    Height            = models.FloatField()
    Width             = models.FloatField()
    Num_Fans          = models.PositiveIntegerField()
    Num_Heatsinks     = models.PositiveIntegerField()
    Previous_Price    = models.FloatField()
    Current_Price     = models.FloatField()
    Links             = models.ForeignKey('AirCooler_Links', on_delete=models.PROTECT)
    Lowest_Price_Link = models.URLField()

    pass


class GPU_Links(models.Model):
    ID = models.ForeignKey('GPU', on_delete=models.CASCADE, null=False, blank=False)
    Amazon_URL = models.URLField()
    Newegg_URL = models.URLField()
    BestBuy_URL = models.URLField()
    pass


class GPU(models.Model):
    pass


class Motherboard_Links(models.Model):
    ID = models.ForeignKey('Motherboard', on_delete=models.CASCADE, null=False, blank=False)
    Amazon_URL = models.URLField()
    Newegg_URL = models.URLField()
    BestBuy_URL = models.URLField()
    pass


class Motherboard(models.Model):
    pass


class RAM_Links(models.Model):
    ID = models.ForeignKey('RAM', on_delete=models.CASCADE, null=False, blank=False)
    Amazon_URL = models.URLField()
    Newegg_URL = models.URLField()
    BestBuy_URL = models.URLField()
    pass


class RAM(models.Model):
    pass


class PSU_Links(models.Model):
    ID = models.ForeignKey('PSU', on_delete=models.CASCADE, null=False, blank=False)
    Amazon_URL = models.URLField()
    Newegg_URL = models.URLField()
    BestBuy_URL = models.URLField()
    pass


class PSU(models.Model):
    Ratings = (
        ('Bronze', 'Bronze'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Platinum', 'Platinum')
    )
    
    Connectivity = (
        ('Full Modular', 'Full Modular'),
        ('Semi Modular', 'Semi Modular'),
        ('None Modular', 'None Modular'),
    )

    Size = (
        ('ATX', 'ATX'),
        ('Mini ATX', 'Mini ATX'),
        ('Micro ATX', 'Micro ATX'),
    )

    ID                = models.CharField(primary_key=True)
    Manufacturer      = models.ForeignKey('Manufacturer')
    Wattage           = models.IntegerField()
    Rating            = models.CharField(choices=Ratings, max_length=10)
    Connection        = models.CharField(choices=Connectivity, max_length=15)
    Size              = models.CharField(choices=Size, max_length=11)
    Previous_Price    = models.FloatField()
    Current_Price     = models.FloatField()
    Links             = models.ForeignKey('PSU_Links', on_delete=models.PROTECT)
    Lowest_Price_Link = models.URLField()
    pass


class Case_Links(models.Model):
    ID = models.ForeignKey('Case', on_delete=models.CASCADE, null=False, blank=False)
    Amazon_URL = models.URLField()
    Newegg_URL = models.URLField()
    BestBuy_URL = models.URLField()
    pass


class Case(models.Model):
    
    InSize = (
        ('ATX', 'ATX'),
        ('Mini ATX', 'Mini ATX'),
        ('Micro ATX', 'Micro ATX'),
    )

    ID                = models.CharField(primary_key=True)
    Manufacturer      = models.ForeignKey('Manufacturer')
    Size              = models.CharField(choices=InSize, max_length=11)
    Height            = models.FloatField()
    Width             = models.FloatField()
    RGB               = models.BooleanField()
    Color             = models.CharField(default='#RRGGBB', max_length=8) #Write the color value as a hex string
    Has_fans          = models.BooleanField()
    Num_fans          = models.IntegerField()
    Previous_Price    = models.FloatField()
    Current_Price     = models.FloatField()
    Links             = models.ForeignKey('Case_Links', on_delete=models.PROTECT)
    Lowest_Price_Link = models.URLField()
    pass
