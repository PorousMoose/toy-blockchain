# -*- coding: utf-8 -*-
from datetime import datetime
import hashlib as hasher
import json


class InvalidProofException(Exception):
    message = 'THE PROOF OF WORK IS INVALID'

class Block:
    def __repr__(self):
        return json.dumps(dict(
            data=self.data,
            #timestamp=self.timestamp,
            hash=self.hash,
            proof=self.proof,
            index=self.index
        ))

    def __init__(self, data, proof, parent):
        self.data = data
        self.proof = proof
        #self.timestamp = self.get_timestamp()
        self.parent_hash = parent.hash
        self.index = parent.index + 1
        self.hash = self.hash_self()
        if not self.prove_self():
            raise InvalidProofException

    def hash_self(self):
        sha = hasher.sha256()
        to_hash = str({
            'parent_hash': self.parent_hash,
            'index': self.index,
            'data': self.data,
            #'timestamp': self.timestamp,
            'proof': self.proof
        })
        sha.update(to_hash.encode('utf-8'))
        return sha.hexdigest()

    def prove_self(self):
        if not self.hash.startswith('000'):
            return False
        else:
            return True

    def get_timestamp(self):
        return datetime.now().isoformat()


class Genesis_Block(Block):
    def __init__(self):
        #self.timestamp = self.get_timestamp()
        self.data = 'GENESIS BLOCK'
        self.hash = '0'
        self.index = 0
        self.proof = 0


def add_block(chain, data, proof=None):
    block = Block(data, proof, last(chain))
    chain.append(block)
    return chain


def create_blockchain(data=[]):
    chain = [Genesis_Block()]

    for datum in data:
        chain = add_block(chain, datum)

    return chain

def last(l):
    return l[len(l) - 1]
