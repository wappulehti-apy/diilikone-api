from flask import Blueprint, jsonify, request, abort

from diilikone.models import Provision, DealGroup
import validators

provision = Blueprint('provision', __name__, url_prefix='/provision')


@provision.route('')
def get():
    deal_size = request.args.get('deal_size', 25, type=int)
    if 'group_id' not in request.args:
        group_deal_size = 0
    else:
        group_id = request.args.get('group_id')
        if not validators.uuid(group_id):
            abort(400)
        group = DealGroup.query.get_or_404(group_id)
        group_deal_size = group.total_size
    deal_size += group_deal_size
    provision = Provision.query.filter_by(quantity=deal_size).first_or_404()
    return jsonify(
        {'price_per_magazine': str(provision.price_per_magazine)}
    ), 200
