from web3 import Web3
from web3.middleware import geth_poa_middleware

APIURL = "https://mainnet.infura.io/v3/e7d4cf0138ed4b49a16824c73860a63a"

web3 = Web3(Web3.HTTPProvider(APIURL))

transaction = web3.eth.get_transaction(
    "0xf782c90e85d3753ac4b2ac34767e647e5962027c0de39cab4c7d0cefb3c94bab"
)

print("Block Hash: ", transaction["blockHash"].hex())
print("Block No.: ", transaction["blockNumber"])
print("From:  ", transaction["from"])
print("Value:  ", transaction["value"])
print("To:  ", transaction["to"])
print("Gas:  ", transaction["gas"])
print("Gas Price:  ", transaction["gasPrice"])
print("Hash:  ", transaction["hash"].hex())
print("Input:  ", transaction["input"].hex())
print("Nonce:  ", transaction["nonce"])
print("Signature:  ", transaction["s"].hex())
