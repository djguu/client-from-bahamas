import os
import re

from app import app
from flask import request

NEEDED_ARGS = ['email', 'fiscal_id', 'name']


@app.route('/store-bahamas-client/<invoice_id>')
def register(invoice_id):
    for key in NEEDED_ARGS:
        if key not in request.args:
            return "Missing or invalid argument. Please check if all parameters are correct", 400
    return request.args, 200


@app.route('/retrieve-bahamas-client/<invoice_id>')
def retrieve(invoice_id):
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    return invoice_id, 200


def valid_name(name):
    return True


def valid_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    if re.search(regex, email):
        return True
    else:
        return False


def valid_fiscal_id(fiscal_id):
    return True
