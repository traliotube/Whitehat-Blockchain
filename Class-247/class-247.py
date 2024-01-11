for nonce in range(15):
    equation = 25 - 5 + nonce
    if equation == 24:
        print(
            f"Verified {nonce}"
        )  # display as "verified" and mention the nonce value at which it got verified.
        break
    else:
        print(f"Not Verified {nonce}")  # display as " not verified"
