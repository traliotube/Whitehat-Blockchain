# --------------253 Proj----------------
from web3 import Web3
import time


ganache_url = "http://127.0.0.1:7545"

web3_ganache_connection = Web3(Web3.HTTPProvider(ganache_url))

Alice_account = "0x59C60Ad1f8717207BBF0e93326C636C4f72Ff80a"
James_account = "0x0313942760F0478304f12cB360627DD3D7CA19b5"
Ryan_account = "0xDe6cD05264AAad25e64E69FD87b1158e886A9edd"


nonce1 = web3_ganache_connection.eth.get_transaction_count(Alice_account)

transaction_data1 = {
    "nonce": nonce1,
    "to": James_account,
    "value": web3_ganache_connection.to_wei(21.5, "ether"),
    "gas": 21000,
    "gasPrice": web3_ganache_connection.to_wei(50, "gwei"),
}

private_key1 = "0xe706adc566220ed0fcea8f8c3ba24f727df689c090cdcafcca734b8efab42e1c"

singed_transaction1 = web3_ganache_connection.eth.account.sign_transaction(
    transaction_data1, private_key1
)
transaction_hash1 = web3_ganache_connection.eth.send_raw_transaction(
    singed_transaction1.rawTransaction
)

print(web3_ganache_connection.to_hex(transaction_hash1))


# -----------------
print("Wait for few seconds Transaction is in progress...")
time.sleep(5)
# -----------------


nonce2 = web3_ganache_connection.eth.get_transaction_count(James_account)

transaction_data2 = {
    "nonce": nonce2,
    "to": Ryan_account,
    "value": web3_ganache_connection.to_wei(32.7, "ether"),
    "gas": 21000,
    "gasPrice": web3_ganache_connection.to_wei(40, "gwei"),
}

private_key2 = "0x6ea0800763ccc615bf957dbbd853d6bf5825e46d3ece30080acb70dc33ac9ef7"

singed_transaction2 = web3_ganache_connection.eth.account.sign_transaction(
    transaction_data2, private_key2
)
transaction_hash2 = web3_ganache_connection.eth.send_raw_transaction(
    singed_transaction2.rawTransaction
)

print(web3_ganache_connection.to_hex(transaction_hash2))
