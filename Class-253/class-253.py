from web3 import Web3

APIURL = "HTTP://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(APIURL))

for i in range(0, 2):
    BlockData = web3.eth.get_block(i)
    print(f"Number: {BlockData['number']}")
    print(f"Hash: {BlockData['hash'].hex()}")
    print(f"Parent Hash: {BlockData['parentHash'].hex()}")
    print(f"Nonce: {BlockData['nonce'].hex()}")
    print(f"Transactions: {BlockData['transactions']}")
    print("--------------------------------------------")


transactions = web3.eth.get_transaction(
    "0xe67c45de4a50a70a0606e5e6784f70eaadbe3510e879cf75f936c9e893b2ac6f"
)
print(f"Transaction Data: {transactions} \n")
print(f"To: {transactions['to']}")
print(f"From: {transactions['from']}")
print(f"Value: {transactions['value']}")
print("-------------------------------------------- \n")
