import pytest
from flask import url_for

from tests.factories import ProductTypeFactory


@pytest.mark.usefixtures('request_ctx', 'database')
class TestProvision(object):
    @pytest.fixture
    def product_types(self):
        return [
            ProductTypeFactory(name='t-paita M', stock=5, price=10.00),
            ProductTypeFactory(name='Laukku', stock=5, price=30.00)
        ]

    def test_returns_200(self, client, product_types):
        response = client.get(url_for('product_types.index'))
        assert response.status_code == 200

    def test_returns_correct_data(self, client, product_types):
        response = client.get(url_for('product_types.index'))
        assert response.json['data'] == [
            {
                'id': str(product_types[1].id),
                'name': 'Laukku',
                'left_in_stock':5,
                'price':'30.00'
            },
            {
                'id': str(product_types[0].id),
                'name': 't-paita M',
                'left_in_stock':5,
                'price':'10.00'
            }
        ]

    def test_returns_empty_array_if_no_product_types(self, client):
        response = client.get(url_for('product_types.index'))
        assert response.json['data'] == []
