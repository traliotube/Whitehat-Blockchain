from web3 import Web3
from web3.middleware import geth_poa_middleware

APIURL = "HTTP://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(APIURL))

acc1 = "0x1CdbB3F64FcB29C0137E3ab7A4477E8Ae4AC6d79"
acc2 = "0xd07896e57b9e9e34dF8dABF8F47230c8A0516980"

privateKey = "0x0efe939de7e6a536cb6fa9356dba9b1bd320b67a5138ad088c89ce9e5ed39527"

nonce = web3.eth.get_transaction_count(acc1)

tx = {
    "nonce": nonce,
    "to": acc2,
    "value": web3.to_wei(1.5, "ether"),
    "gas": 25000,
    "gasPrice": web3.to_wei(1, "gwei"),
}

signedTx = web3.eth.account.sign_transaction(tx, privateKey)
send = web3.eth.send_raw_transaction(signedTx.rawTransaction)
print(web3.to_hex(send))
