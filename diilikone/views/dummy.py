from flask import Blueprint, jsonify

dummy = Blueprint('dummy', __name__)


@dummy.route('/')
def index():
    return jsonify({'Hello': 'World'})
