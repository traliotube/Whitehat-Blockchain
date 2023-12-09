from web3 import Web3
from web3.middleware import geth_poa_middleware

url = "https://mainnet.infura.io/v3/e7d4cf0138ed4b49a16824c73860a63a"

web3 = Web3(Web3.HTTPProvider(url))

blockdata = web3.eth.get_block("latest")
print("\n\n\nLatest Block Data: ", blockdata)

print("\n\nTransaction Count: ", web3.eth.get_block_transaction_count("latest"))
print("\n\nFee history: ", web3.eth.fee_history(1, "latest"))
