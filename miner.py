# -*- coding: utf-8 -*-
import requests
import json
import random

def make_request(body):
    body = json.dumps(body)
    r = requests.post('http://localhost:5000/add', data=body)
    if r.text == 'bad proof':
        return False
    else:
        return True


def mine(data):
    for d in data:
        success = False
        body = {
            'data': d,
            'proof': random.randint(0, 1000)
        }
        while not success:
            success = make_request(body)
            body['proof'] += 1
        print(f'added {d} to blockchain')
        print('congrats, you mined 1 blarnbuck')
        print('\n')


if __name__ == '__main__':
    data = (f'superblarn{i}' for i in range(100))
    mine(data)
