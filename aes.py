from tkinter import *
from tkinter import ttk
from Crypto.Util.Padding import pad, unpad
import hashlib
import base64
import importlib
from Crypto.Cipher import AES
from Crypto import Random
from hashlib import md5
from Crypto.Random import get_random_bytes
from binascii import hexlify, unhexlify


class AEScbc:
    def __init__(self, key):
        password = key.encode('utf-8')
        self.key = md5(password).digest()

    def encrypt(self, data):
        # inic.vector:
        vector = get_random_bytes(AES.block_size)
        # print(vector)
        encryption_cipher = AES.new(self.key, AES.MODE_CBC, vector)
        return vector + encryption_cipher.encrypt(pad(data,  AES.block_size))

    def decrypt(self, data):
        file_vector = data[:AES.block_size]
        decryption_cipher = AES.new(self.key, AES.MODE_CBC, file_vector)
        return unpad(decryption_cipher.decrypt(data[AES.block_size:]), AES.block_size)


def clean():
    ResultEntry.delete(0, END)
    TextEntry.delete(0, END)
    KeyEntry.delete(0, END)

# function for choice:


def validate():
    value = option.get()
    mode = mode1.get()
    # raktas:
    k = str(KeyEntry.get())
    # text to encrypt
    s = str(TextEntry.get())

    # sifravimas ebc
    if value == "1" and mode == "2":
        print("sifravimas")
        # print(k)
        cipher = AES.new(k.encode("utf-8"), AES.MODE_ECB)
        msg = cipher.encrypt(s)
        print(msg.hex())

        # writing encrypted text to file
        with open('data.txt', 'w') as f:
            f.write(msg.hex())

        # showing the result:
        with open('data.txt', 'r') as f:
            ResultEntry.insert(0, f.read())

        decipher = AES.new(k.encode("utf-8"), AES.MODE_ECB)
        msg_dec = decipher.decrypt(msg)
        print(msg_dec)

    # atsifravimas ECB
    elif value == "2" and mode == "2":
        print("desifravimasECB")
        decipher = AES.new(k.encode("utf-8"), AES.MODE_ECB)
        msg_dec = decipher.decrypt(s)
        print(msg_dec)
        ResultEntry.insert(0, msg_dec)

    # sifravimas CBC
    elif value == "1" and mode == "1":
        print("sifravimasCBC")
        msg = s.encode('utf-8')
        pwd = k

        encrypted = AEScbc(pwd).encrypt(msg)
     
        
        # writing encrypted text to file
        with open('data.txt', 'w') as f:
            f.write(encrypted.hex())

        # showing the result:
        with open('data.txt', 'r') as f:
            ResultEntry.insert(0, f.read())

    # desifravimas CBC
    elif value == "2" and mode == "1":
        print("desifravimasCBC")
       
        decrypted = AEScbc(k).decrypt(s).decode('utf-8')
       
        print(decrypted)
    

    else:
        print("An option must be selected")


# ------------GUI--------
# main screen
master = Tk()
master.title('SIFRAVIMAS AES ALGORITMU')
option = StringVar()
mode1 = StringVar()
k = StringVar()

# field for text:
Label(master, text="Jusu tekstas", font=(
    "Arial", 15)).grid(row=2, sticky=W, padx=5)
TextEntry = Entry(master)
TextEntry.grid(row=2, column=1)

# choose an operation:
Label(master, text="Operacija:", font=(
    "Arial", 15)).grid(row=3, sticky=W, padx=5)
O1 = Radiobutton(master, text="Sifravimas",  value=1, var=option)
O1.grid(row=3, column=1)
O2 = Radiobutton(master, text="Atsifravimas",  value=2, var=option)
O2.grid(row=4, column=1)

# choose mode:
Label(master, text="Moda:", font=("Arial", 15)).grid(row=5, sticky=W, padx=5)
M1 = Radiobutton(master, text="CBC",  value=1, var=mode1)
M1.grid(row=5, column=1)
M2 = Radiobutton(master, text="ECB",  value=2, var=mode1)
M2.grid(row=6, column=1)

# key:
Label(master, text="Raktas", font=("Arial", 15)).grid(row=7, sticky=W, padx=5)
KeyEntry = Entry(master)
KeyEntry.grid(row=7, column=1)


# button to get result
button = Button(master, text='GO', width=5, command=validate)
button.grid(row=8, column=1)


# field for result:
Label(master, text="Rezultatas", font=(
    "Arial", 15)).grid(row=9, sticky=W, padx=5)
ResultEntry = Entry(master)
ResultEntry.grid(row=9, column=1)

# button to clean result
button = Button(master, text='ISVALYTI', width=8, command=clean)
button.grid(row=10, column=1)

# size of the page
master.geometry('400x400')
master.mainloop()
