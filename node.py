# -*- coding: utf-8 -*-
import json

from flask import Flask, request

from blockchain import add_block, create_blockchain, last, InvalidProofException
node = Flask(__name__)

node_transactions = create_blockchain()
print(node_transactions)




@node.route('/trans', methods=['GET'])
def transaction():
    if request.method == 'GET':
        # return node_transactions
        return repr(node_transactions)

@node.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        try:
            request_data = json.loads(request.data)
        except:
            return 'bad json'

        if 'proof' not in request_data or 'data' not in request_data:
            return 'missing keys'

        try:
            add_block(node_transactions, **request_data)
            return 'successfully created block'
        except InvalidProofException:
            return 'bad proof'

if __name__ == '__main__':
    node.run()
