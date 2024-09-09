from django.test import TestCase, Client
from .models import ChocolateProduct

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_strong_cocoa_ratio(self):
        product = ChocolateProduct.objects.create(
            name_product = "Läderach",
            price = "110.00",  # Note this should be a Decimal, not a string
            description = "Premium chocolate from Swiss with the freshest ingredients to create memorable moments of joy!",
            type = "Dark Chocolate",
            cocoa_ratio = 80,
            app_name = "Bonagit Store",
            name = "Shaine Glorvina Mathea",
            my_class = "PBP B"
        )
        self.assertTrue(product.is_cocoa_ratio_strong)