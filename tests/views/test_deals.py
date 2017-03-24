import json

import pytest
from flask import url_for
from flexmock import flexmock
from tests.factories import DealGroupFactory, ProductTypeFactory

from diilikone.models import Deal, User
from diilikone.services import email


@pytest.mark.usefixtures('request_ctx', 'database')
class DealsPOSTTestCase(object):
    @pytest.fixture(autouse=True)
    def mocked_email_confirmation(self):
        mocked = flexmock(email)
        mocked.should_receive('send_confirmation_email')

    @pytest.fixture
    def deal_group(self):
        return DealGroupFactory(
            id='9e96eb6d-f113-483e-8ce8-ce5296004269',
            name='Tietokilta'
        )

    @pytest.fixture
    def product_types(self):
        return [
            ProductTypeFactory(id='a0d0c7c3-bcf3-49a9-9dd7-68faa14b7ba6'),
            ProductTypeFactory(id='e8d3767f-9051-4192-bc6a-0013b3cab871')
        ]

    @pytest.fixture
    def deal(self):
        return Deal.query.first()

    @pytest.fixture
    def salesperson(self):
        return User.query.filter_by(email='vesa@fastmonkeys.com').one()

    @pytest.fixture
    def response(self, client, data):
        return client.post(url_for('deals.post'), data=json.dumps(data))


class TestDealsPostFullData(DealsPOSTTestCase):
    @pytest.fixture
    def data(self, deal_group, product_types):
        return {
            'group_id': '9e96eb6d-f113-483e-8ce8-ce5296004269',
            'size': 25,
            'product_ids': [
                'a0d0c7c3-bcf3-49a9-9dd7-68faa14b7ba6',
                'e8d3767f-9051-4192-bc6a-0013b3cab871'
            ],
            'salesperson': {
                'first_name': 'Vesa',
                'last_name': 'Uimonen',
                'email': 'vesa@fastmonkeys.com',
                'phone_number': '+358405409708',
                'class_year': 'N'
            }
        }

    def test_returns_200(self, response):
        assert response.status_code == 200

    def test_creates_salesperson_with_correct_data(
        self, response, salesperson
    ):
        assert salesperson.first_name == 'Vesa'
        assert salesperson.last_name == 'Uimonen'
        assert salesperson.email == 'vesa@fastmonkeys.com'
        assert salesperson.phone_number == '+358405409708'
        assert salesperson.class_year == 'N'

    def test_creates_deal_with_correct_data(
        self, response, deal, deal_group, product_types, salesperson
    ):
        assert deal.deal_group == deal_group
        assert deal.size == 25
        assert set(deal.product_types) == set(product_types)
        assert deal.salesperson == salesperson


class TestDealsPostMinimumData(DealsPOSTTestCase):
    @pytest.fixture
    def data(self):
        return {
            'group_id': None,
            'size': 25,
            'product_ids': [],
            'salesperson': {
                'first_name': 'Vesa',
                'last_name': 'Uimonen',
                'email': 'vesa@fastmonkeys.com',
                'phone_number': '+358405409708',
                'class_year': 'N'
            }
        }

    def test_returns_200(self, response):
        assert response.status_code == 200

    def test_creates_deal_with_correct_data(
        self, response, deal, deal_group, product_types, salesperson
    ):
        assert deal.deal_group is None
        assert deal.size == 25
        assert deal.product_types == []
        assert deal.salesperson == salesperson
