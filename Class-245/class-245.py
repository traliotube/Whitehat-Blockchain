from web3 import Web3

APIURL = "https://mainnet.infura.io/v3/e7d4cf0138ed4b49a16824c73860a63a"

web3 = Web3(Web3.HTTPProvider(APIURL))

gas_price = web3.eth.gas_price

safeLow = web3.from_wei(int(gas_price * 0.9), "gwei")
avg = web3.from_wei(int(gas_price * 1), "gwei")
fast = web3.from_wei(int(gas_price * 1.1), "gwei")
fastest = web3.from_wei(int(gas_price * 1.2), "gwei")

print("Safe Low: ", safeLow)
print("Average/ Gas Price: ", avg)
print("Fast: ", fast)
print("Fastest: ", fastest)
