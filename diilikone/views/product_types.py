from flask import Blueprint, jsonify

from diilikone.models import ProductType

product_types = Blueprint(
    'product_types',
    __name__,
    url_prefix='/product-types'
)


@product_types.route('')
def index():

    product_types = ProductType.query.order_by('name')

    data = [
        {
            'id': str(product_type.id),
            'name': product_type.name,
            'price': str(product_type.price),
            'left_in_stock': product_type.left_in_stock
        }
        for product_type in product_types
    ]

    return jsonify({'data': data}), 200
