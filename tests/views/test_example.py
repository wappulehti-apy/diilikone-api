import pytest
from flask import url_for


@pytest.mark.usefixture('ctx')
class TestExample:
    def test_example(self, client):
        response = client.get(url_for('dummy.index'))
        assert response.json == {'Hello': 'World'}
