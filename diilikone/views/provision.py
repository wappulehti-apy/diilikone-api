from flask import Blueprint, jsonify, request

from diilikone.models import Provision

provision = Blueprint('provision', __name__, url_prefix='/provision')


@provision.route('')
def get():
    deal_size = request.args.get('deal_size', 25, type=int)
    provision = Provision.query.filter_by(quantity=deal_size).first_or_404()
    return jsonify(
        {'price_per_magazine': str(provision.price_per_magazine)}
    ), 200
