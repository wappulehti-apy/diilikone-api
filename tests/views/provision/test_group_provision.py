import pytest
from flask import url_for

from tests.factories import (DealFactory, DealGroupFactory,
                             GroupProvisionFactory)


@pytest.mark.usefixtures('request_ctx', 'database')
class TestProvision(object):
    @pytest.fixture
    def provisions(self):
        return [
            GroupProvisionFactory(quantity=25, price_per_magazine=0.2),
            GroupProvisionFactory(quantity=50, price_per_magazine=0.25),
            GroupProvisionFactory(quantity=150, price_per_magazine=0.40),
            GroupProvisionFactory(quantity=350, price_per_magazine=0.45),
            GroupProvisionFactory(quantity=375, price_per_magazine=0.50)
        ]

    @pytest.fixture
    def deal_group(self):
        group = DealGroupFactory()
        DealFactory(size=25, deal_group=group)
        DealFactory(size=100, deal_group=group)
        DealFactory(size=200, deal_group=group)
        return group

    def test_url(self):
        assert url_for('provision.get_group') == '/provision/group'

    def test_returns_400_if_no_group_id(self, client, provisions):
        response = client.get(url_for('provision.get_group'))
        assert response.status_code == 400

    def test_returns_200(self, client, provisions, deal_group):
        args = {'group_id': deal_group.id}
        response = client.get(url_for('provision.get_group', **args))
        assert response.status_code == 200

    def test_returns_correct_price_per_magazine(
        self,
        client,
        provisions,
        deal_group
    ):
        args = {'deal_size': 50, 'group_id': deal_group.id}
        response = client.get(url_for('provision.get_group', **args))
        assert response.json == {'price_per_magazine': '0.50'}

    def test_returns_404_for_unknown_deal_size(
        self,
        client,
        provisions,
        deal_group
    ):
        args = {'deal_size': 69, 'group_id': deal_group.id}
        response = client.get(url_for('provision.get_group', **args))
        assert response.status_code == 404

    def test_group_id_is_non_existing(self, client, provisions, deal_group):
        response = client.get(url_for(
            'provision.get_group',
            **{
                'deal_size': 25,
                'group_id': 'd9f9f199-70b4-44a8-99ad-a5203859f37e'
            }
        ))
        assert response.status_code == 404

    def test_group_id_is_invalid_should(self, client, provisions, deal_group):
        response = client.get(
            url_for(
                'provision.get_group',
                **{
                    'deal_size': 25,
                    'group_id': 'invalid-uuid'
                }
            )
        )
        assert response.status_code == 400
