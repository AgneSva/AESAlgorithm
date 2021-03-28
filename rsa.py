from tkinter import *
from tkinter import ttk
import math
from binascii import hexlify, unhexlify
import random


'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while (e > 0):
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if (temp_phi == 1):
        return d + phi


def inverse(e, phi):
    a, b, u = 0, phi, 1
    while(e > 0):
        q = b // e
        e, a, b, u = b % e, u, e, a-q*u
    if (b == 1):
        return a % phi
    else:
        print("Must be coprime!")


def generate_keypair(p, q):
    #n = pq
    n = p * q

    # Phi is the totient of n
    phi = (p-1) * (q-1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key

    d = inverse(e, phi)
    print("phi=", phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)

    return ((e, n), (d, n))


def clean():
    ResultEntry.delete(0, END)
    TextEntry.delete(0, END)
    pEntry.delete(0, END)
    qEntry.delete(0, END)


def isPrime(num):
    if num > 1:

        for i in range(2, num):
            if (num % i) == 0:
                return False
                break
        else:
            return True

    else:
        return False

def encrypt(pk, plaintext):
    key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    #letter to ascii decimal
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    #Return the array of bytes as a string
    
    return plain

# function for choices:
def validate():
    # sifravimas ar desifravimas
    value = option.get()
    # text to encrypt
    x = str(TextEntry.get())

    if value == "1":
        print("sifravimas")
        p = int(pEntry.get())   
        q = int(qEntry.get())

        # tikrinam ar pirminis
        if (isPrime(p) != True or isPrime(q) != True):

            raise ValueError('Both numbers must be prime.')

      
        public, private = generate_keypair(p, q)
        print(" public key is ", public,
              " and yprivate key is ", private)

        # viesa rakta i faila:
        with open('data.txt', 'w') as f:
            f.write(str(public))

        encrypted_msg = encrypt(public, x)
        print(" encrypted message is: ")
        print (''.join(map(lambda xi: str(xi), encrypted_msg)))

        # rezultata i faila:
        with open('result.txt', 'w') as f:
            f.write(''.join(map(lambda xi: str(xi), encrypted_msg)))

        # showing the result:
        with open('result.txt', 'r') as f:
            ResultEntry.insert(0, f.read())

    elif value == "2":
        print("desifravimas")
        #paimti public key is failo
        with open('data.txt', 'r') as f:
            public=f.read()
        
  
        
        #print (decrypt(public, x))

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


# p:
Label(master, text="p (prime number)", font=(
    "Arial", 15)).grid(row=7, sticky=W, padx=5)
pEntry = Entry(master)
pEntry.grid(row=7, column=1)


# q:
Label(master, text="q (prime number)", font=(
    "Arial", 15)).grid(row=8, sticky=W, padx=5)
qEntry = Entry(master)
qEntry.grid(row=8, column=1)

# button to get result
button = Button(master, text='GO', width=5, command=validate)
button.grid(row=9, column=1)


# field for result:
Label(master, text="Rezultatas", font=(
    "Arial", 15)).grid(row=10, sticky=W, padx=5)
ResultEntry = Entry(master)
ResultEntry.grid(row=10, column=1)

# button to clean result
button = Button(master, text='ISVALYTI', width=8, command=clean)
button.grid(row=11, column=1)

# size of the page
master.geometry('400x400')
master.mainloop()
