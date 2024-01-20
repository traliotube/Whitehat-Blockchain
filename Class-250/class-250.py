# Predefined code begins
import hashlib
import json
from time import time


class Block(object):
    def __init__(self):
        self.chain = []
        self.new_transactions = []
        self.count = 0
        self.new_block(
            previous_hash="No previous Hash. Since this is the first block.", proof=100
        )

    def new_block(self, proof, previous_hash=None):
        block = {
            "Block No": self.count,
            "timestamp": time(),
            "transactions": self.new_transactions
            or "No Transactions First Genesis Block",
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

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof_condition = False

        while check_proof_condition is False:
            compare_proof = new_proof**2 - previous_proof**2
            string_compare_proof = str(compare_proof).encode()
            encode_proof = hashlib.sha256(string_compare_proof)
            hash_proof = encode_proof.hexdigest()
            print("Getting proof of work:", hash_proof)
            if hash_proof[:4] == "0000":
                check_proof_condition = True
            else:
                new_proof = new_proof + 1

        return new_proof

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

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        block["Current hash"] = hex_hash
        return hex_hash

    # Predefined code ends
    # add the code for chain_valid() function

    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            currentBlock = chain[block_index]
            if currentBlock["previous_hash"] != previous_block["Current hash"]:
                return False

            previous_proof = previous_block["nonce"]
            currentProof = currentBlock["nonce"]
            print(f"Previous Nonce: {previous_proof}\n Current Proof: {currentProof}")
            compare_proof = currentProof**2 - previous_proof**2
            print(f"Comparation: {compare_proof}")
            string_compare_proof = str(compare_proof).encode()
            encode_proof = hashlib.sha256(string_compare_proof)
            hash_proof = encode_proof.hexdigest()
            print(f"Hash: {hash_proof}")
            if hash_proof[:4] != "0000":
                return False
            previous_block = currentBlock
            block_index = block_index + 1

        return True


# Predefined code begins
blockchain = Block()
transaction1 = blockchain.transaction("Satoshi", "Mike", "5 ETH")
transaction2 = blockchain.transaction("Mike", "Satoshi", "1 ETH")
transaction3 = blockchain.transaction("Satoshi", "Hal Finney", "5 ETH")

previous_block = blockchain.last_block()

previous_proof = previous_block["nonce"]

proof = blockchain.proof_of_work(previous_proof)
print("Found proof of work at:", proof)

previous_hash = blockchain.hash(previous_block)
print("Previous block hash:", previous_hash)

block = blockchain.new_block(proof, previous_hash)
# Predefined code ends

# Add the code to validate the block in blockchain

if blockchain.chain_valid(blockchain.chain):
    print("Blockchain is valid")
else:
    print("Blockchain is not valid")
