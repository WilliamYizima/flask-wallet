from flask import Blueprint, jsonify, request

from flask_wallet.ext.db import db
from flask_wallet.ext.db.models import Receipts

bp = Blueprint("api/receipts", __name__)

#TODO  implementar flask_restful 
@bp.route("/", methods=['POST'])
def insert():
    receipts = request.form
    print(receipts)

    return 'ok'