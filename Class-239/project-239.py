import hashlib
from time import time
import json

chain = []


def block(proof, previous_hash=None):
    transaction = {"sender": "Satoshi", "reciever": "Mike", "amount": "5 ETH"}
    data = {
        "block_height": 12913586,
        "timestamp": time(),
        "transaction": transaction,
        "Block Reward": "2.046327048499942521 ETH",
        "Uncles Reward": "0",
        "Difficulty": 7293278291370357,
        "Total Difficulty": "28,070,572,181,009,216,929,429",
        "Size": "81,010 bytes",
        "Gas Used": 14993305,
        "Gas Limit": 14999907,
        "proof": proof,
        "previous_hash": previous_hash,
    }
    chain.append(block)
    print("Block Info", data)
    hash = hashlib.sha512(json.dumps(data).encode()).hexdigest()
    print("Block Hash", hash)


block(000, "First Block")
