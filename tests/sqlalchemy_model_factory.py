from factory import Factory

from diilikone.extensions import db


class SQLAlchemyModelFactory(Factory):
    """
    Factory for SQLAlchemy models.
    """

    ABSTRACT_FACTORY = True

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Create an instance of the model, and save it to the database."""

        obj = model_class(*args, **kwargs)
        db.session.add(obj)
        db.session.commit()
        return obj
