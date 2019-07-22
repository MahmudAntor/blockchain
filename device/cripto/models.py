from django.db import models

class Self(models.Model):
    public_key = models.IntegerField(default=7919)
    private_key = models.IntegerField(default=7927)
    df_key = models.IntegerField(blank=True, null=True)
    partial = models.IntegerField(blank=True, null=True)

class Miner(models.Model):
    public_key = models.IntegerField(default=19)
    df_key = models.IntegerField(blank=True, null=True)
    partial = models.IntegerField(blank=True, null=True)