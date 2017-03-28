from flask import Blueprint, jsonify

from diilikone.models import DealGroup

deal_groups = Blueprint('deal_groups', __name__, url_prefix='/deal-groups')


@deal_groups.route('')
def index():
    deal_groups = DealGroup.query.order_by('name')
    data = [
        {
            'id': str(group.id),
            'name': group.name,
            'target_description': group.target_description,
            'percentage': group.percentage

        }
        for group in deal_groups
    ]
    return jsonify({'data': data}), 200
