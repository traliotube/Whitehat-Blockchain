from web3 import Web3
from web3.middleware import geth_poa_middleware

APIURL = "HTTP://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(APIURL))

acc1 = "0x5B7A4b42fD7a4eF694157F0e3Ea53C5464a82734"
acc2 = "0x00C817f2CA08D20c366AF606654165791E784cD6"

privateKey = "0xb51194d61a3ad6e3820078f2b7b02858b79b41a5bba530456fc6b86be9799152"

nonce = web3.eth.get_transaction_count(acc1)

tx = {
    "nonce": nonce,
    "to": acc2,
    "value": web3.to_wei(15.5, "ether"),
    "gas": 21000,
    "gasPrice": web3.to_wei(50, "gwei"),
}

signedTx = web3.eth.account.sign_transaction(tx, privateKey)
send = web3.eth.send_raw_transaction(signedTx.rawTransaction)
print(web3.to_hex(send))
