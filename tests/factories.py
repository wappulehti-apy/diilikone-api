import diilikone.models

from .sqlalchemy_model_factory import SQLAlchemyModelFactory


class ProvisionFactory(SQLAlchemyModelFactory):
    class Meta:
        model = diilikone.models.Provision

    quantity = 25
    price_per_magazine = 1.2
