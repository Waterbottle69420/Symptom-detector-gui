import tkinter as tk
import autodocdef as ad

email= ad.readbin("v_ownerinfo.bin")
email = email['Email']

root = tk.Tk()
def mail():
    ad.webbrowser.open('https://mail.google.com/')
root.title('AutoDoc')
tk.Label(root, text = 'The OPD can be reached by dropping an email at:', font=('Courier', 20)).pack()
tk.Label(root, text = email, font=('Courier', 20)).pack()
tk.Button(root,text = 'Continue', command = mail,font=('Courier', 20)).pack()
root.mainloop()
