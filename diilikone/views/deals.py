from flask import Blueprint, jsonify, request

from diilikone.extensions import db
from diilikone.models import Deal, ProductType, User
from diilikone.schemas import DealSchema

deals = Blueprint('deals', __name__, url_prefix='/deals')


@deals.route('', methods=['POST'])
def post():
    data = request.get_json(force=True)
    data, errors = DealSchema().load(data)
    if errors:
        return jsonify({'errors': errors}), 400

    salesperson = User(**data['salesperson'])
    deal = Deal(
        size=data['size'],
        deal_group_id=data['deal_group_id'],
        salesperson=salesperson
    )

    for product_type_id in data['product_types']:
        product_type = ProductType.query.get(product_type_id)
        deal.product_types.append(product_type)
    db.session.add_all([salesperson, deal])
    db.session.commit()
    return jsonify({}), 200
