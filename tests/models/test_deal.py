import pytest
from sqlalchemy_utils import assert_non_nullable

from tests.factories import DealFactory


@pytest.mark.usefixtures('database')
class TestDeal(object):
    @pytest.mark.parametrize(
        'column',
        (
            'id',
            'size',
            'deal_group_id',
            'salesperson_id'
        )
    )
    def test_non_nullable_columns(self, column):
        assert_non_nullable(DealFactory(), column)

    def test_repr(self):
        deal = DealFactory.build()
        assert repr(deal) == "<Deal size=%s, salesperson='%s'>" % (
            deal.size, deal.salesperson.name
        )
