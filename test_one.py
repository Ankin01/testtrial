import pytest

from testi.models import Product

pytestmark = pytest.mark.django_db

class TestProductModel:
    def test_save(self):
        product = Product.objects.create(
            name="Sample product",
            price=500
        )
        assert product.name == "Sample product"
        assert product.price == 500