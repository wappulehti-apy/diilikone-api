import pytest
from flask import url_for

from tests.factories import (DealFactory, DealGroupFactory,
                             IndividualProvisionFactory)


@pytest.mark.usefixtures('request_ctx', 'database')
class TestProvision(object):
    @pytest.fixture
    def provisions(self):
        return [
            IndividualProvisionFactory(quantity=25, price_per_magazine=1.2),
            IndividualProvisionFactory(quantity=50, price_per_magazine=1.25),
            IndividualProvisionFactory(quantity=150, price_per_magazine=1.40)
        ]

    @pytest.fixture
    def deal_group(self):
        group = DealGroupFactory()
        DealFactory(size=25, deal_group=group)
        DealFactory(size=100, deal_group=group)
        return group

    def test_url(self):
        assert url_for('provision.get') == '/provision/individual'

    def test_returns_200(self, client, provisions):
        response = client.get(url_for('provision.get'))
        assert response.status_code == 200

    def test_returns_correct_price_per_magazine(self, client, provisions):
        response = client.get(url_for('provision.get', **{'deal_size': 50}))
        assert response.json == {'price_per_magazine': '1.25'}

    def test_defaults_to_25_deal_size(self, client, provisions):
        response = client.get(url_for('provision.get'))
        assert response.json == {'price_per_magazine': '1.20'}

    def test_returns_404_for_unknown_deal_size(self, client, provisions):
        response = client.get(url_for('provision.get', **{'deal_size': 69}))
        assert response.status_code == 404

    def test_takes_group_total_size_into_account(
        self, client, provisions, deal_group
    ):
        response = client.get(
            url_for(
                'provision.get',
                **{'deal_size': 25, 'group_id': str(deal_group.id)}
            )
        )
        assert response.json == {'price_per_magazine': '1.40'}

    def test_group_id_is_non_existing(self, client, provisions, deal_group):
        response = client.get(url_for(
            'provision.get',
            **{
                'deal_size': 25,
                'group_id': 'd9f9f199-70b4-44a8-99ad-a5203859f37e'
            }
        ))
        assert response.status_code == 404

    def test_group_id_is_invalid(self, client, provisions, deal_group):
        response = client.get(
            url_for(
                'provision.get',
                **{
                    'deal_size': 25,
                    'group_id': 'd9f9f199-70b4-44a8-99ad-alol59f37e'
                }
            )
        )
        assert response.status_code == 400
