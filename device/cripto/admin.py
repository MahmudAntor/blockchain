from django.contrib import admin

# Register your models here.
from .models import Self, Miner, GlobalChain, Hash

admin.site.register(Self)
admin.site.register(Miner)
admin.site.register(GlobalChain)
admin.site.register(Hash)
