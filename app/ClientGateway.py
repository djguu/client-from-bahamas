import os

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
    print(app.config['SQLALCHEMY_DATABASE_URL'])
    return invoice_id, 200
    # return app.config['SECRET_KEY']

