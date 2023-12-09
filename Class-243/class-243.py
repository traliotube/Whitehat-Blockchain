from web3 import Web3
from web3.middleware import geth_poa_middleware

APIURL = "https://mainnet.infura.io/v3/e7d4cf0138ed4b49a16824c73860a63a"

web3 = Web3(Web3.HTTPProvider(APIURL))

blockdata = web3.eth.get_block(18746598)
print("\n\n\nBlock Data: ", blockdata)

print("\n\nGas Used: ", blockdata["gasUsed"])
print("\n\nTotal difficulty: ", blockdata["difficulty"])
print("\n\n\nTransactions: ", blockdata["transactions"])

print(
    "\n\n\n\nData: ",
    web3.eth.get_transaction(
        "0x5536d39968a0e43861f58c2c81d4d8923aa6c1396a8bf35b95011f59ee1f779d"
    ),
),
