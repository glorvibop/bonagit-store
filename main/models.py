from django.db import models
import uuid  # tambahkan baris ini di paling atas
from django.contrib.auth.models import User

class ChocolateProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=0, max_digits=5)
    description = models.TextField()
    type = models.CharField(max_length=255)
    cocoa_ratio = models.IntegerField()

    @property
    def is_cocoa_ratio_strong(self):
        return self.cocoa_ratio > 70