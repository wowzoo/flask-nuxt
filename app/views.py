import json

from flask import Blueprint, request

bp = Blueprint('views', __name__)


@bp.route('/', methods=['GET', 'POST'])
def check_status():
    return {"status": "ok"}


@bp.route('/hello', methods=['GET'])
def hello():
    return 'hello world!'


@bp.route('/event', methods=['POST'])
def event():
    return 'post event'
