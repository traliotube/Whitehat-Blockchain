from web3 import Web3
import json
import requests

infura_url = "https://mainnet.infura.io/v3/e7d4cf0138ed4b49a16824c73860a63a"
web3 = Web3(Web3.HTTPProvider(infura_url))

gasPrice = web3.eth.gas_price

print("safeLow", web3.from_wei(int(gasPrice * 0.9), "gwei"))
print("average", web3.from_wei(int(gasPrice * 0.9), "gwei"))
print("fast", web3.from_wei(int(gasPrice * 0.9), "gwei"))
print("fastest", web3.from_wei(int(gasPrice * 0.9), "gwei"))
block = web3.eth.get_block("latest")
print("Block number:", block["number"])

gasEth = gasPrice / 10**18
gasUSD = gasEth * 2228.52
print(f"Gas Price In Eth: {gasEth}. In USD: {gasUSD}")

transaction = web3.eth.get_transaction(block["transactions"][-1].hex())
print(f"Transaction: {transaction}")
detail = web3.eth.get_transaction(block["transactions"][-1].hex())
gasEstimate = web3.eth.estimate_gas({"to": detail["to"], "from": detail["to"]})
print(f"Gas Limit: {detail['gas']}")
print(f"Gas Used: {gasEstimate}")
