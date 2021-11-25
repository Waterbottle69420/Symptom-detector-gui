import autodocdef as ad
import tkinter as tk
from tkinter import messagebox as mb

root = tk.Tk()

def check():
    a = ent.get()
    ret = ad.idcheck(a)
    if ret == True:
        ad.pathold(a)
        root.destroy()
        ad.os.system('ad_checkup.py')
    else:
        mb.showinfo('AutoDoc', 'ID has not been registered. Please contact owner.')
        root.destroy()
        ad.os.system('AutoDoc.py')

root.title('AutoDoc Interface - ID check')

root.geometry('400x220')

label_head = tk.Label(root, text = 'AutoDoc', font=('Courier', 25))

label_head.pack()

label_sub = tk.Label(root, text = 'Enter Patient ID\n', font=('Courier', 20))

label_sub.pack()

ent = tk.Entry(root, font=('Courier', 18))

ent.pack()

label_space= tk.Label(root, text = '', font=('Courier', 10))

label_space.pack()

b1 = tk.Button(root, text = 'Enter', font = ('Courier', 18), command = check)

b1.pack()

root.mainloop()

