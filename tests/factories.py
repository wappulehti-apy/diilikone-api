import factory

import diilikone.models

from .sqlalchemy_model_factory import SQLAlchemyModelFactory


class ProvisionFactory(SQLAlchemyModelFactory):
    class Meta:
        model = diilikone.models.Provision

    quantity = 25
    price_per_magazine = 1.2


class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = diilikone.models.User

    first_name = 'John'
    last_name = 'Doe'
    email = factory.Sequence(lambda n: 'john.doe{0}@email.com'.format(n))
    phone_number = '0401231234'
    guild = 'Tietokilta'
    class_year = 'N'
