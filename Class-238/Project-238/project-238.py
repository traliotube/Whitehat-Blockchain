import hashlib

filename = "./Project-238/tohash.jpg"

with open(filename, "rb") as f:
    data = f.read()
    imageHash = hashlib.sha256(data).hexdigest()
    print(imageHash)
