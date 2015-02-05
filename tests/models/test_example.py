import pytest

from diilikone.extensions import db
from diilikone.models import Dummy


@pytest.mark.usefixtures('database')
class TestExample:
    def test_example(self):
        d = Dummy()
        db.session.add(d)
        db.session.commit()
        assert Dummy.query.count() == 1
