from flask import Blueprint, jsonify

from diilikone.models import DealGroup

deal_status = Blueprint(
    'deal_status',
    __name__,
    url_prefix='/deal-status'
)


@deal_status.route('/<secret_id>')
def index(secret_id):
    deal_group = DealGroup.query.filter_by(secret_id=secret_id).first_or_404()

    data = [
        {
            'group_name': deal_group.name,
            'total_size': deal_group.total_size,
            'total_money': 'TODO calculate',
            'percentage': deal_group.percentage,
            'target_description': deal_group.target_description,
            'salespersons': [
                {
                    'name': deal.salesperson.name,
                    'size': deal.size
                } for deal in deal_group.deals
            ]
        }
    ]

    return jsonify({'data': data}), 200
