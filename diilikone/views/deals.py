from flask import Blueprint, jsonify, request

from diilikone.extensions import db
from diilikone.models import Deal, DealGroup, ProductType, User
from diilikone.schemas import DealSchema
from diilikone.services import email

deals = Blueprint('deals', __name__, url_prefix='/deals')


@deals.route('', methods=['POST'])
def post():
    data = request.get_json(force=True)
    data, errors = DealSchema().load(data)
    if errors:
        return jsonify({'errors': errors}), 400

    salesperson = User(**data['salesperson'])
    deal = Deal(
        size=data.get('size'),
        deal_group_id=data.get('group_id', None),
        salesperson=salesperson
    )

    for product_type_id in data.get('product_ids'):
        product_type = ProductType.query.get(product_type_id)
        deal.product_types.append(product_type)
    db.session.add_all([salesperson, deal])
    db.session.commit()
    email.send_confirmation_email(deal)
    return jsonify({}), 200


@deals.route('/top-groups', methods=['GET'])
def top_groups():
    not_empty_deals = filter(
        lambda deal_group: deal_group.total_size > 0, DealGroup.query.all()
    )

    top3 = sorted(
        not_empty_deals, key=lambda deal_group: deal_group.total_size,
        reverse=True
    )[:3]

    data = [
        {
            'name': deal_group.name,
            'size': deal_group.total_size
        } for deal_group in top3
    ]

    return jsonify({'data': data}), 200
