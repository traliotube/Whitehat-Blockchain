from web3 import Web3
from tkinter import *

root = Tk()

root.title("My Ethereum App")
root.geometry("500x200")
root.configure(background="white")

# Setting labels
block_name_label = Label(
    root, text="Ethereum Block", font=("Helvetica", 18, "bold"), bg="white"
)
block_name_label.place(relx=0.5, rely=0.15, anchor=CENTER)
block_entry = Entry(root, text="This is Entry Widget", bd=2)

block_entry.place(relx=0.5, rely=0.35, anchor=CENTER)
gasused_info_label = Label(root, bg="white", font=("bold", 10))
gasused_info_label.place(relx=0.5, rely=0.38, anchor=CENTER)
gaslimit_info_label = Label(root, bg="white", font=("bold", 10))
gaslimit_info_label.place(relx=0.5, rely=0.5, anchor=CENTER)


APIURL = "https://mainnet.infura.io/v3/e7d4cf0138ed4b49a16824c73860a63a"
web3 = Web3(Web3.HTTPProvider(APIURL))


# Write Code for Task 01 below.
def ethereum_block():
    number = int(block_entry.get())
    block_data = web3.eth.get_block(number)
    transaction = web3.eth.get_transaction(block_data["transactions"][-1].hex())
    Value = transaction["value"]
    valueInEther = Value / 10**18
    valueInDollar = valueInEther * 2228.52
    # Write Code for Task 02 below.
    gas = transaction["gas"]
    gasused_info_label["text"] = f"Value: ${valueInDollar}"
    gaslimit_info_label["text"] = f"Gas: {gas}"
    block_name_label["text"] = f"Ethereum Block {number}"

    block_entry.destroy()
    search_btn.destroy()


search_btn = Button(
    root, text="Search Ethereum transaction fee", command=ethereum_block, relief=FLAT
)
search_btn.place(relx=0.5, rely=0.48, anchor=CENTER)
root.mainloop()
