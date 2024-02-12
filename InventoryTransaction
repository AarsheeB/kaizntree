from django.db import models

class InventoryTransaction(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20)  # 'IN' for incoming, 'OUT' for outgoing
    quantity = models.IntegerField()
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.item.name}"
