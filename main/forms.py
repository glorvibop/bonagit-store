from django.forms import ModelForm
from main.models import ChocolateProduct
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = ChocolateProduct
        fields = ["product_name", "price", "description", "type", "cocoa_ratio"]

    def clean_product_name(self):
        product_name = self.cleaned_data["product_name"]
        return strip_tags(product_name)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
    
    def clean_type(self):
        type = self.cleaned_data["type"]
        return strip_tags(type)