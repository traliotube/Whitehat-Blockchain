from tkinter import *
from web3 import Web3
from PIL import ImageTk, Image

root = Tk()
root.title("Account Details")
root.configure(background="white")

ganache_url = "https://mainnet.infura.io/v3/e7d4cf0138ed4b49a16824c73860a63a"

web3 = Web3(Web3.HTTPProvider(ganache_url))

img = ImageTk.PhotoImage(Image.open("./Class-257/Project/image.png"))
panel = Label(root, image=img, bg="white")
panel.pack(side="top")

frame = Frame(root, bg="white", padx=5, pady=5)

Label(frame, text="Account No. 1: ", fg="black", bg="white").grid(
    row=0, column=0, sticky=W, pady=10
)
acc1 = Entry(frame)
acc1.grid(row=0, column=1, sticky=W, padx=10, pady=20)

Label(frame, text="Account No. 2: ", fg="black", bg="white").grid(
    row=1, column=0, sticky=W, pady=10
)
acc2 = Entry(frame)
acc2.grid(row=1, column=1, sticky=W, padx=10, pady=20)

Label(frame, text="Account No. 3: ", fg="black", bg="white").grid(
    row=2, column=0, sticky=W, pady=10
)
acc3 = Entry(frame)
acc3.grid(row=2, column=1, sticky=W, padx=10, pady=20)

Label(frame, text="Account No. 4: ", fg="black", bg="white").grid(
    row=3, column=0, sticky=W, pady=10
)
acc4 = Entry(frame)
acc4.grid(row=3, column=1, sticky=W, padx=10, pady=20)

Label(frame, text="Account No. 5: ", fg="black", bg="white").grid(
    row=4, column=0, sticky=W, pady=10
)
acc5 = Entry(frame)
acc5.grid(row=4, column=1, sticky=W, padx=10, pady=20)


result = Text(root, height=10, width=45, bg="white", fg="black")


def checkBalance():
    accno = []
    accno.append(acc1.get())
    accno.append(acc2.get())
    accno.append(acc3.get())
    accno.append(acc4.get())
    accno.append(acc5.get())
    for i in range(5):
        result.insert(
            END,
            f"Account No. {i+1} {(web3.eth.get_balance(accno[i]))*0.000000000000000001} Eth\n",
        )


frame.pack()

btn = Button(root, text="Check Balance", command=checkBalance).pack(fill="both")
result.pack(fill="both")

root.mainloop()
