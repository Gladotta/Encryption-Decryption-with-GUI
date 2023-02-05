import tkinter as tk
from cryptography.fernet import Fernet
def key_gen():
  key = Fernet.generate_key()
  print('key from key_gen ',key)
  with open("pass.key", "wb") as key_file: key_file.write(key)
key_gen()
def call_key():
     return open("pass.key", "rb").read()

def code_message(message):
  key = call_key()
  a = Fernet(key)
  coded_slogan = a.encrypt(message)
  return coded_slogan

def decode_message(coded_slogan):
  key = call_key()
  b = Fernet(key)
  decoded_slogan = b.decrypt(coded_slogan)
  return decoded_slogan.decode()
    
def GUI():
 def getResult():
   
    choice = v.get()
    
    if choice == 'e':   
        x1 = ent1.get().encode()
        lab1['text'] = code_message(x1)
        canvas1.create_window(170,220,window=lab1)


    else:
        x1 = ent1.get()
        lab1['text'] = decode_message(x1)
        canvas1.create_window(170,220,window=lab1)
 
 win = tk.Tk()
 win.title('endec')
 win.minsize(width=350, height = 300)
 canvas1= tk.Canvas(win, width=350, height=300)
 canvas1.pack()

 ent1 = tk.Entry(win)
 canvas1.create_window(170,130, window=ent1)
 lab1=tk.Label()
 canvas1.create_window(170,195, window=lab1)
 but1=tk.Button(text ="submit", command=getResult)
 canvas1.create_window(170,160, window=but1)

 v=tk.StringVar()
 v.set("e")

 b=tk.Radiobutton(win, text="Encrypt", variable=v, value='e')
 canvas1.create_window(170,70, window=b)
 b2=tk.Radiobutton(win, text="Decrypt", variable=v, value='d')
 canvas1.create_window(170,100, window=b2)


 win.mainloop()
GUI()