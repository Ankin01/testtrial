import pytest

from testi.models import Product, Firm

from django.test import TestCase

pytestmark = pytest.mark.django_db

class TestProductModel:


    def test_save(self):
        product = Product.objects.create(
            name="Sample product",
            price=500
        )
        assert product.name == "Sample product"
        assert product.price == 500

class TestFirmModel(TestCase):

    def setUp(self):
        new_firm = Firm.objects.create(name="Arsenal")
        new_firm.save()

    def test_firm_exists(self):
        firm_name = Firm.objects.get(name="Arsenal")
        self.assertEqual(firm_name, "Arsenal")



