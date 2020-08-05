from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/store-bahamas-client/<invoice_id>')
def register(invoice_id):
    NEEDED_ARGS = ['email', 'fiscal_id', 'name']
    args = request.args
    for key in NEEDED_ARGS:
        if key not in args:
            return "Missing or invalid argument. Please check if all parameters are correct", 400
    return request.args, 200


@app.route('/retrieve-bahamas-client/<invoice_id>')
def retrieve(invoice_id):
    return invoice_id, 200


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(debug=True, host='127.0.0.1', port=port)