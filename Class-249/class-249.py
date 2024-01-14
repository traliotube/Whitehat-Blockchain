import hashlib

PB_current_hash = "573de6af99199bdc7ae9534891d512afbc2b1473f2f6a5784e0c078d67a60bf9"

str = "Alice sends James 5 Eth amount"

newHash = hashlib.sha256(str.encode()).hexdigest()

if newHash == PB_current_hash:
    print("Transaction is valid")
else:
    print("Transaction is invalid")
