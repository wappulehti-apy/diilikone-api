from diilikone.models import DealGroup, ProductType, User
from marshmallow import fields, Schema
from marshmallow.validate import Length


def validate_deal_group_id(group_id):
    if group_id is None:
        return True
    return DealGroup.query.get(group_id) is not None


def validate_product_type_id(product_type_id):
    return ProductType.query.get(product_type_id) is not None


def validate_email(email):
    return User.query.filter_by(email=email).count() == 0


class UserSchema(Schema):
    first_name = fields.Str(required=True, validate=Length(max=255))
    last_name = fields.Str(required=True, validate=Length(max=255))
    email = fields.Email(required=True, validate=validate_email)
    phone_number = fields.Str(required=True, validate=Length(max=20))
    guild = fields.Str(required=True, validate=Length(max=100))
    class_year = fields.Str(required=True, validate=Length(max=10))


class DealSchema(Schema):
    deal_group_id = fields.UUID(
        validator=validate_deal_group_id,
        allow_none=True
    )
    size = fields.Integer(required=True, validator=lambda x: x % 25 == 0)
    salesperson = fields.Nested(UserSchema)
    product_types = fields.List(
        fields.UUID(validator=validate_product_type_id),
        allow_none=True
    )


class DealGroupSchema(Schema):
    deal_group_id = fields.UUID(validator=validate_deal_group_id)
    deals = fields.Nested(DealSchema, many=True)
