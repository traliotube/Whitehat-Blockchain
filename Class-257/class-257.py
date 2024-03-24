from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frame Demo")
root.configure(background="white")

logo = ImageTk.PhotoImage(Image.open("./Class-257/logo.jpeg"))
logoLabel = Label(root, image=logo).pack(side="top")

frame = Frame(root, padx=5, pady=5, bg="white")

Label(frame, text="Account No. 1: ", fg="black", bg="white").grid(
    row=0, column=0, sticky=W, pady=10
)
Label(frame, text="Account No. 2: ", fg="black", bg="white").grid(
    row=1, column=0, sticky=W, pady=10
)
Label(frame, text="Private Key: ", fg="black", bg="white").grid(
    row=2, column=0, sticky=W, pady=10
)
Label(frame, text="ETH: ", fg="black", bg="white").grid(
    row=3, column=0, sticky=W, pady=10
)
Label(frame, text="Gas Price (Gwei): ", fg="black", bg="white").grid(
    row=4, column=0, sticky=W, pady=10
)
Label(frame, text="Gas Limit (Gwei): ", fg="black", bg="white").grid(
    row=5, column=0, sticky=W, pady=10
)

frame.pack()

root.mainloop()
