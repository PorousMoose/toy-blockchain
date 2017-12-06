# -*- coding: utf-8 -*-
import requests
import json
from blockchain import add_block, create_blockchain, InvalidProofException

def main():
    r = requests.get('http://localhost:5000/trans')
    chain_repr = json.loads(r.text)

    genesis = chain_repr[0]
    validate_genesis(genesis)

    chain = create_blockchain()
    for block in chain_repr[1:]:
        try:
            add_block(chain, block['data'], block['proof'])
        except InvalidProofException:
            print('The chain has been tampered with')

    print_chain(chain)


def print_chain(chain):
    for block in chain:
        print(f'data: {block.data}')
        print(f'index: {block.index}')


def validate_genesis(genesis):
    assert genesis['data'] == 'GENESIS BLOCK'
    assert genesis['hash'] == '0'
    assert genesis['proof'] == 0
    assert genesis['index'] == 0

if __name__ == '__main__':
    main()
