from web3 import Web3

url = "https://sepolia.infura.io/v3/e7d4cf0138ed4b49a16824c73860a63a"

web3 = Web3(Web3.HTTPProvider(url))

student = "0x44b55C5437Df5a1E5e8C46F5dD5E0A2C02D6D594"
teacher = "0xf636974779073814951Be8C2254B00A1989E627e"

private_key = ""

nonce = web3.eth.get_transaction_count(student)

transactionData = {
    "nonce": nonce,
    "to": teacher,
    "value": web3.to_wei(0.0001, "ether"),
    "gas": 21000,
    "gasPrice": web3.to_wei(10, "gwei"),
}

signedTransaction = web3.eth.account.sign_transaction(transactionData, private_key)
transactionHash = web3.eth.send_raw_transaction(signedTransaction.rawTransaction)

print(web3.to_hex(transactionHash))
