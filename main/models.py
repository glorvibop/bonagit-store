from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DateField(auto_now_add=True)
    description = models.TextField()
    cocoa_ratio = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5