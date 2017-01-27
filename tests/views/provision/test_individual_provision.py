import pytest
from flask import url_for
from tests.factories import IndividualProvisionFactory


@pytest.mark.usefixtures('request_ctx', 'database')
class TestIndividualProvision(object):
    @pytest.fixture
    def provisions(self):
        return [
            IndividualProvisionFactory(quantity=25, price_per_magazine=1.2),
            IndividualProvisionFactory(quantity=50, price_per_magazine=1.25),
            IndividualProvisionFactory(quantity=150, price_per_magazine=1.40)
        ]

    def test_url(self):
        assert url_for('provision.get_individual') == '/provision/individual'

    def test_returns_200(self, client, provisions):
        response = client.get(url_for('provision.get_individual'))
        assert response.status_code == 200

    def test_returns_correct_price_per_magazine(self, client, provisions):
        url = url_for('provision.get_individual', **{'deal_size': 50})
        response = client.get(url)
        assert response.json == {'price_per_magazine': '1.25'}

    def test_defaults_to_25_deal_size(self, client, provisions):
        response = client.get(url_for('provision.get_individual'))
        assert response.json == {'price_per_magazine': '1.20'}

    def test_returns_404_for_unknown_deal_size(self, client, provisions):
        url = url_for('provision.get_individual', **{'deal_size': 69})
        response = client.get(url)
        assert response.status_code == 404
