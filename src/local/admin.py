from django.contrib import admin

from .models import BlockHeader, PolicyHeader, Transactions, Block, BlockChain


admin.site.register(BlockHeader)
admin.site.register(PolicyHeader)
admin.site.register(Transactions)
admin.site.register(Block)
admin.site.register(BlockChain)
