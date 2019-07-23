from django.db import models

class Device(models.Model):
    public_key = models.IntegerField(blank=True, null=True)
    partial = models.IntegerField(blank=True, null=True)
    dh_key = models.IntegerField(blank=True, null=True)
    status = models.BooleanField(default=False)

class Miner(models.Model):
    public_key = models.IntegerField(default=19)
    private_key = models.IntegerField(default=17)
    dh_key = models.IntegerField(blank=True, null=True)
    partial = models.IntegerField(blank=True, null=True)