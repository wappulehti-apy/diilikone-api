import pytest
from sqlalchemy_utils import assert_max_length, assert_non_nullable

from tests.factories import DealGroupFactory


@pytest.mark.usefixtures('database')
class TestDealGroup(object):
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
