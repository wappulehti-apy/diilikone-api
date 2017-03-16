import pytest
import sqlalchemy as sa
from sqlalchemy_utils import assert_max_length, assert_non_nullable
from tests.factories import UserFactory


@pytest.mark.usefixtures('database')
class TestUser(object):
    @pytest.mark.parametrize(
        'column',
        (
            'id',
            'email',
            'first_name',
            'last_name'
        )
    )
    def test_non_nullable_columns(self, column):
        assert_non_nullable(UserFactory(), column)

    @pytest.mark.parametrize(
        ('column', 'max_length'),
        (
            ('email', 255),
            ('first_name', 255),
            ('last_name', 255),
            ('guild', 100),
            ('class_year', 1),
            ('phone_number', 20)
        )
    )
    def test_max_lengths(self, column, max_length):
        assert_max_length(UserFactory(), column, max_length)

    def test_email_unique(self):
        UserFactory(email='email@email.com')
        with pytest.raises(sa.exc.IntegrityError):
            UserFactory(email='email@email.com')

    def test_name_property(self):
        user = UserFactory(first_name='John', last_name='Doe')
        assert user.name == 'John Doe'

    def test_repr(self):
        user = UserFactory.build()
        assert repr(user) == "<User name='%s'>" % user.name
