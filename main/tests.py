from django.test import TestCase, Client
from .models import Product

class mainTest(TestCase):
    def setUp(self):
        # Membuat data produk untuk digunakan dalam test
        self.product = Product.objects.create(
            name="Läderach",
            price=25.00,
            description="Cokelat segar premium dari Swiss, terkenal dengan FrischSchoggi™ dan truffle berkualitas.",
            cocoa_ratio=70
        )

    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/nonexistent/')
        self.assertEqual(response.status_code, 404)

    # def test_product_detail_view(self):
    #     # Test untuk memastikan detail produk dapat diakses
    #     url = f'/products/{self.product.id}/'
    #     response = Client().get(url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'product_detail.html')

    def test_strong_cocoa_content(self):
        # Test untuk memastikan metode custom pada model bekerja dengan benar
        self.assertTrue(self.product.cocoa_ratio > 50)