import pytest
from sqlalchemy_utils import assert_non_nullable

from diilikone.extensions import db
from tests.factories import DealFactory, ProductTypeFactory


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

    def test_left_in_stock(self):
        product_type = ProductTypeFactory(stock=5)
        for _ in range(3):
            deal = DealFactory()
            deal.product_types.append(product_type)
        db.session.commit()

        assert product_type.left_in_stock == 2
