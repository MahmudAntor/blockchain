from django.db import models
from device.models import Device
from django.conf import settings


class BlockHeader(models.Model):
    hash = models.CharField(max_length=100)

class PolicyHeader(models.Model):
    GENESIS = 1
    STORE = 2
    ACCESS = 3
    MONITOR = 4
    REMOVE = 5
    ACTION_TYPES = (
        (GENESIS, 'Genesis'),
        (STORE, 'Store'),
        (ACCESS, 'Access'),
        (MONITOR, 'Monitor'),
        (REMOVE, 'Remove'),
    )
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    requested_action = models.CharField(max_length=100)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, blank=True, null=True)
    action = models.PositiveSmallIntegerField(choices=ACTION_TYPES)

class Transactions(models.Model):
    GENESIS = 1
    STORE = 2
    ACCESS = 3
    MONITOR = 4
    REMOVE = 5
    ACTION_TYPES = (
        (GENESIS, 'Genesis'),
        (STORE, 'Store'),
        (ACCESS, 'Access'),
        (MONITOR, 'Monitor'),
        (REMOVE, 'Remove'),
    )
    prev_transaction = models.ForeignKey('self', on_delete=models.PROTECT ,blank=True, null=True)
    transaction_number = models.IntegerField()
    device = models.ForeignKey(Device, on_delete=models.CASCADE, blank=True, null=True)
    transaction_type = models.PositiveSmallIntegerField(choices=ACTION_TYPES)

class Block(models.Model):
    Block_header = models.ForeignKey(BlockHeader, on_delete=models.CASCADE)
    Policy_header = models.ForeignKey(PolicyHeader, on_delete=models.CASCADE)
    Transactions = models.ManyToManyField(Transactions)

class BlockChain(models.Model):
    Block_chain = models.ManyToManyField(Block)
