from django.forms import ModelForm
from main.models import ChocolateProduct

class ProductForm(ModelForm):
    class Meta:
        model = ChocolateProduct
        fields = ["product_name", "price", "description", "type", "cocoa_ratio"]