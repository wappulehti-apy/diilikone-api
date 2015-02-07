import pytest
from flask import url_for

from tests.factories import DealGroupFactory


@pytest.mark.usefixtures('request_ctx', 'database')
class TestProvision(object):
    @pytest.fixture
    def deal_groups(self):
        return [
            DealGroupFactory(name='Tietokilta'),
            DealGroupFactory(name='Fyysikkokilta')
        ]

    def test_returns_200(self, client, deal_groups):
        response = client.get(url_for('deal_groups.index'))
        assert response.status_code == 200

    def test_returns_correct_data(self, client, deal_groups):
        response = client.get(url_for('deal_groups.index'))
        assert response.json['data'] == [
            {
                'id': str(deal_groups[1].id), 'name': 'Fyysikkokilta'
            },
            {
                'id': str(deal_groups[0].id), 'name': 'Tietokilta'
            }
        ]

    def test_returns_empty_array_if_no_deal_groups(self, client):
        response = client.get(url_for('deal_groups.index'))
        assert response.json['data'] == []
