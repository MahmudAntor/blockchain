from django.contrib import admin

# Register your models here.
from .models import Self, Miner

admin.site.register(Self)
admin.site.register(Miner)