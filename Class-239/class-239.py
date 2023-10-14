import hashlib
from time import time
import json

chain = []


def block(proof, previous_hash=None):
    transaction = {"sender": "Alex", "reciever": "Max", "amount": "5 ETH"}
    data = {
        "index": 1,
        "timestamp": time(),
        "transactions": transaction,
        "gas": 0.1,
        "proof": proof,
        "previous_hash": previous_hash,
    }
    chain.append(block)
    print("Block Info", data)
    hash = hashlib.sha256(json.dumps(data).encode()).hexdigest()
    print("Block Hash", hash)


block(000, "First Block")
