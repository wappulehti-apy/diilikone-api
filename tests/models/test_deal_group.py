import pytest
from sqlalchemy_utils import assert_max_length, assert_non_nullable

from tests.factories import DealFactory, DealGroupFactory


@pytest.mark.usefixtures('database')
class TestDealGroup(object):
    @pytest.fixture
    def deal_group(self):
        group = DealGroupFactory()
        DealFactory(size=25, deal_group=group)
        DealFactory(size=100, deal_group=group)
        return group

    @pytest.mark.parametrize(
        'column',
        (
            'id',
            'name',
            'owner_id'
        )
    )
    def test_non_nullable_columns(self, column):
        assert_non_nullable(DealGroupFactory(), column)

    def test_name_max_length(self):
        assert_max_length(DealGroupFactory(), 'name', 255)

    def test_repr(self):
        deal_group = DealGroupFactory.build()
        assert repr(deal_group) == "<DealGroup name='%s'>" % deal_group.name

    def test_total_size_sums_deal_sizes(self, deal_group):
        assert deal_group.total_size == 125
