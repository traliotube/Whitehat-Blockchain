import hashlib
import json
from time import time


class Block(object):
    def __init__(self):
        self.chain = []
        self.new_transactions = []
        self.count = 0
        self.new_block(previous_hash="0")

    def new_block(self, previous_hash=None):
        block = {
            "Block No": self.count,
            "timestamp": time(),
            "transactions": self.new_transactions or 0,
            "gasfee": 0.1,
            "previous_hash": previous_hash or self.hash(self.chain[-1]),
        }
        self.new_transactions = []
        self.count += 1
        self.chain.append(block)

        return block

    def last_block(self):
        return self.chain[-1]

    def transaction(self, sender, receiver, amount):
        self.new_transactions.append(
            {
                "sender": (hashlib.sha256(sender.encode())).hexdigest(),
                "receiver": (hashlib.sha256(receiver.encode())).hexdigest(),
                "amount": amount,
            }
        )
        return self.last_block

    def hash(self, block):
        string_object = json.dumps(block)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        self.chain.append(("Current Hash: ", hex_hash))
        return hex_hash


blockchain = Block()
blockchain.transaction("A", "B", 100)
blockchain.transaction("A", "C", 56)
blockchain.transaction("B", "C", 75)
blockchain.new_block()
blockchain.transaction("D", "B", 62)
blockchain.transaction("A", "D", 55)
blockchain.transaction("B", "D", 315)
blockchain.new_block()

print(blockchain.chain)
