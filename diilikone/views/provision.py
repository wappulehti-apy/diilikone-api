import validators
from flask import abort, Blueprint, jsonify, request

from diilikone.models import DealGroup, GroupProvision, IndividualProvision

provision = Blueprint('provision', __name__, url_prefix='/provision')


@provision.route('/individual')
def get_individual():
    deal_size = request.args.get('deal_size', 25, type=int)
    provision = (
        IndividualProvision.query.filter_by(quantity=deal_size).first_or_404()
    )
    return jsonify(
        {'price_per_magazine': str(provision.price_per_magazine)}
    ), 200


@provision.route('/group')
def get_group():
    deal_size = request.args.get('deal_size', 25, type=int)
    if 'group_id' not in request.args:
        abort(400)
    else:
        group_id = request.args.get('group_id')
        if not validators.uuid(group_id):
            abort(400)
        group = DealGroup.query.get_or_404(group_id)
        group_deal_size = group.total_size
    deal_size += group_deal_size
    provision = (
        GroupProvision.query.filter_by(quantity=deal_size).first_or_404()
    )
    return jsonify(
        {'price_per_magazine': str(provision.price_per_magazine)}
    ), 200
