import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy_utils import assert_non_nullable

from tests.factories import IndividualProvisionFactory


@pytest.mark.usefixtures('database')
class TestProvision(object):
    @pytest.fixture
    def provision(self):
        return IndividualProvisionFactory(
            quantity=25,
            price_per_magazine=1.25
        )

    @pytest.mark.parametrize(
        'column_name',
        [
            'id',
            'quantity',
            'price_per_magazine'
        ]
    )
    def test_non_nullable_columns(self, column_name, provision):
        assert_non_nullable(provision, column_name)

    def test_quantity_is_unique(self):
        IndividualProvisionFactory(quantity=25)
        with pytest.raises(IntegrityError):
            IndividualProvisionFactory(quantity=25)
