# Predefined Code
import hashlib
import json
from time import time


class Block(object):
    def __init__(self):
        self.chain = []
        self.new_transactions = []
        self.count = 0
        self.new_block(previous_hash="0", proof=52)

    def new_block(self, proof, previous_hash=None):
        block = {
            "Block No": self.count,
            "timestamp": time(),
            "transactions": self.new_transactions or "0",
            "gasfee": 0.1,
            "nonce": proof,
            "previous_hash": previous_hash or self.hash(self.chain[-1]),
        }
        self.new_transactions = []
        self.count = self.count + 1
        self.chain.append(block)

        return block

    def last_block(self):
        return self.chain[-1]

    # End of Predefined Code
    # Student code begins

    def proof_of_work(self, previous_proof):
        new_proof = 1
        proofCondition = False

        while proofCondition is False:
            compare = new_proof**2 - previous_proof**2
            hashProof = hashlib.sha256(str(compare).encode()).hexdigest()
            if hashProof[:4] == "0000":
                proofCondition = True
            else:
                new_proof += 1
        return new_proof

    # Student code ends
    # Start of predefined code

    def transaction(self, sender, recipient, amount):
        sender_encoder = hashlib.sha256(sender.encode())
        sender_hash = sender_encoder.hexdigest()
        recipient_encoder = hashlib.sha256(recipient.encode())
        recipient_hash = recipient_encoder.hexdigest()

        transaction_data = {
            "sender": sender_hash,
            "recipient": recipient_hash,
            "amount": amount,
        }
        self.new_transactions.append(transaction_data)
        return self.last_block

    # Start of Predefined Code
    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        block["Current hash"] = hex_hash
        return hex_hash


blockchain = Block()
transaction1 = blockchain.transaction("Satoshi", "Mike", "5 ETH")
transaction2 = blockchain.transaction("Mike", "Satoshi", "1 ETH")
transaction3 = blockchain.transaction("Satoshi", "Hal Finney", "5 ETH")
# end of predefined code

# student code begins
previousBlock = blockchain.last_block()
print(f"Previous Block: {previousBlock}")

previousProof = previousBlock["nonce"]
print(f"Previous Block Proof: {previousProof}")

proof = blockchain.proof_of_work(previousProof)
print(f"Previous Block Proof of Work: {proof}")

previousHash = blockchain.hash(previousBlock)
print(f"Previous Block Hash: {previousHash}")

block = blockchain.new_block(proof, previousHash)
# Students code ends
