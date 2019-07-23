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
    ALLOW = 1
    DENY = 2
    ACTION = (
        (ALLOW, 'Allow'),
        (DENY, 'Deny'),
    )
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    requested_action = models.PositiveSmallIntegerField(choices=ACTION_TYPES)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, blank=True, null=True)
    action = models.PositiveSmallIntegerField(choices=ACTION)

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
    prev_transaction = models.ForeignKey('self', on_delete=models.CASCADE ,blank=True, null=True)
    transaction_number = models.IntegerField()
    device = models.ForeignKey(Device, on_delete=models.CASCADE, blank=True, null=True)
    transaction_type = models.PositiveSmallIntegerField(choices=ACTION_TYPES)
    device_status = models.BooleanField(default=False)

    class Meta:
        get_latest_by = "transaction_number"

class Block(models.Model):
    prev_block = models.ForeignKey('self', on_delete=models.CASCADE ,blank=True, null=True)
    block_header = models.ForeignKey(BlockHeader, on_delete=models.CASCADE)
    policy_header = models.ManyToManyField(PolicyHeader, blank=True)
    transactions = models.ManyToManyField(Transactions, blank=True)

class BlockChain(models.Model):
    block_chain = models.ManyToManyField(Block)
