from django.db import models

class Self(models.Model):
    public_key = models.IntegerField(default=7919)
    private_key = models.IntegerField(default=7927)
    dh_key = models.IntegerField(blank=True, null=True)
    partial = models.IntegerField(blank=True, null=True)

class Miner(models.Model):
    public_key = models.IntegerField(default=19)
    dh_key = models.IntegerField(blank=True, null=True)
    partial = models.IntegerField(blank=True, null=True)

class Hash(models.Model):
    hash = models.CharField(max_length=100)

class GlobalChain(models.Model):
    hashchain = models.ManyToManyField(Hash, blank=True)