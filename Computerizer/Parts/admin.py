from django.contrib import admin
from .models import *

# Register your models here.
admin.register('CPU_Links')
admin.register('CPU')

admin.register('Cooler_Links')
admin.register('Cooler')

admin.register('GPU_Links')
admin.register('GPU')

admin.register('RAM_Links')
admin.register('RAM')

admin.register('Motherboard_Links')
admin.register('Motherboard')

admin.register('PSU_Links')
admin.register('PSU')

admin.register('Case_Links')
admin.register('Case')
