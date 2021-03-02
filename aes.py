from tkinter import *
from tkinter import ttk



def clean():
    ResultEntry.delete(0, END)
    TextEntry.delete(0, END)
    KeyEntry.delete(0, END)

#function for choice:
def validate():
    clean()
    value = option.get()
    mode= mode1.get()
    k=KeyEntry.get()
    #sifravimas CBC

    if value == "1" and mode=="1":
        #print("sifravimas")
        
       
        #text to encrypt
        s=TextEntry.get()
        s.encode('utf-8')
        #then goes to encryption function
        encrypted = AESCipher(k).encrypt(s)
        print('Ciphertext:', encrypted)
        #e = AESCipher(k, 16)
        #print (e)
        #enc_str = e.encrypt(s)
        #ResultEntry.insert(0,enc_str)

    elif value == "2":
        #print("desifravimas")
        k=int(KeyEntry.get())
        if k>26 or k<0:
            print("wrong")
        s=TextEntry.get()
        #then goes to encryption function
       # x = (''.join(map(chr, decryption(s, k))))
       # print (x)
       # ResultEntry.insert(0,x)

    else:
        print("An option must be selected")


#------------GUI--------
#main screen
master= Tk()
master.title('SIFRAVIMAS AES ALGORITMU')
option = StringVar()
mode1 = StringVar()

#field for text:
Label(master,text = "Jusu tekstas",font=("Arial",15)).grid(row = 2, sticky = W,padx=5)
TextEntry=Entry(master)
TextEntry.grid(row=2,column=1)

#choose an operation:
Label(master,text = "Operacija:",font=("Arial",15)).grid(row = 3, sticky = W,padx=5)
O1 = Radiobutton(master, text="Sifravimas",  value=1, var=option)
O1.grid( row=3,column=1 )
O2 = Radiobutton(master, text="Atsifravimas",  value=2, var=option)
O2.grid( row=4,column=1 )

#choose mode:
Label(master,text = "Moda:",font=("Arial",15)).grid(row = 5, sticky = W,padx=5)
M1 = Radiobutton(master, text="CBC",  value=1, var=mode1 )
M1.grid( row=5,column=1 )
M2 = Radiobutton(master, text="EBC",  value=2, var=mode1)
M2.grid( row=6,column=1 )

#key: 
Label(master,text = "Raktas",font=("Arial",15)).grid(row = 7, sticky = W,padx=5)
KeyEntry=Entry(master)
KeyEntry.grid(row=7,column=1)


#button to get result
button = Button(master, text='GO', width=5,command=validate)
button.grid(row=8,column=1)



#field for result:
Label(master,text = "Rezultatas",font=("Arial",15)).grid(row = 9, sticky = W,padx=5)
ResultEntry=Entry(master)
ResultEntry.grid(row=9,column=1)

#button to clean result
button = Button(master, text='ISVALYTI', width=8,command=clean)
button.grid(row=10,column=1)

#size of the page
master.geometry('400x400')
master.mainloop()