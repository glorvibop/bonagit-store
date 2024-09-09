from django.db import models

class ChocolateProduct(models.Model):
    name_product = models.CharField(max_length=255)
    price = models.FloatField
    description = models.TextField()
    type = models.CharField(max_length=255)
    cocoa_ratio = models.IntegerField()
    app_name = models.CharField(max_length=255)
    name =  models.CharField(max_length=255)
    my_class =  models.CharField(max_length=255)

    @property
    def is_cocoa_ratio_strong(self):
        return self.cocoa_ratio > 70