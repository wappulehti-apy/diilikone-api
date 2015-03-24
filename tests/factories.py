import factory

import diilikone.models

from .sqlalchemy_model_factory import SQLAlchemyModelFactory


class IndividualProvisionFactory(SQLAlchemyModelFactory):
    class Meta:
        model = diilikone.models.IndividualProvision

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


class DealGroupFactory(SQLAlchemyModelFactory):
    class Meta:
        model = diilikone.models.DealGroup

    name = 'Fyysikkokilta'
    owner = factory.SubFactory(UserFactory)


class DealFactory(SQLAlchemyModelFactory):
    class Meta:
        model = diilikone.models.Deal

    size = 75
    salesperson = factory.SubFactory(UserFactory)


class ProductTypeFactory(SQLAlchemyModelFactory):
    class Meta:
        model = diilikone.models.ProductType

    name = 'paita M'
    price = 10.50
    stock = 20
