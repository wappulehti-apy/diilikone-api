import pytest
from sqlalchemy_utils import assert_non_nullable

from tests.factories import ProductTypeFactory


@pytest.mark.usefixtures('database')
class TestProductType(object):
    @pytest.mark.parametrize(
        'column',
        (
            'id',
            'name',
            'price',
            'stock'
        )
    )
    def test_non_nullable_columns(self, column):
        assert_non_nullable(ProductTypeFactory(), column)

    def test_repr(self):
        product_type = ProductTypeFactory.build()
        assert repr(product_type) == "<ProductType name='%s', price=%s>" % (
            product_type.name, product_type.price
        )
