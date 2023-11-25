import hashlib, json
from time import time


class Block:
    def __init__(self):
        self.chain = []
        self.new_transactions = []
        self.count = 0
        self.new_block(previous=0)

    def new_block(self, previous=None):
        block = {
            "Block No": self.count,
            "Timestamp": time(),
            "Transactions": self.new_transactions or 0,
            "gasfee": 0.1,
            "previous_hash": previous,
        }

        self.count += 1
        self.chain.append(block)

        block_string = (json.dumps(block)).encode()

        hash = (hashlib.sha256(block_string)).hexdigest()
        self.chain.append(("Current Hash: ", hash))
        return block


block = Block()

print(block.chain)
