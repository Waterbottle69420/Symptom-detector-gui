import autodocdef as ad

from tkinter import messagebox

ad.log('ad home accessed')


import tkinter as tk

from tkinter import *

def b1():
    root.destroy()
    ad.os.system('ad_id_input.py')

def b2():
    root.destroy()
    ad.os.system('ad_command.py')

def b3():
    ad.webbrowser.open('https://www.google.com/search?q=nearby+doctors&oq=nearby+doctors&aqs=chrome..69i57j0l7.3095j0j7&sourceid=chrome&ie=UTF-8')

def b4():
    ad.webbrowser.open('https://docs.google.com/document/d/1HXdEAt5qQ859a5Nxou8PsIiE2l66tW_LyDUXgwlwBXM/edit?usp=sharing')
        

def b5():
    root.destroy()
    while True:
        for i in range(3):
            print("Help Summoned!")
        ad.sound('emergency.mp3')
        ad.sound('emergency_2.mp3')  

def b6():
    root.destroy()
    ad.os.system('ad_command.py')

def b7():
    root.destroy()
    ad.os.system('ad_health.py')

def b8():
    
    ret = ad.readcsv('v_pat.csv')
    tk.messagebox.showinfo('WARNING!', 'Please do not save or modify \
the database which shall be shown!')
    ad.os.system('v_pat.csv')
    

root = tk.Tk()

root.title('AutoDoc Home Page - Personal Edition')

root.geometry('1000x500')

label_head = tk.Label(root, text = 'AutoDoc', font=('Courier', 40))

label_head.pack()

label_sub = tk.Label(root, text = 'By Vineeth Bhat and Ishank Bhatnagar', font=('Courier', 8))

label_sub.pack()

b1 = tk.Button(root, width = 25,text ='Self Diagnosis', command = b1, font=('Courier', 20))

b7 = tk.Button(root,width = 25, text = 'Daily Health Checkup', command = b7,font=('Courier', 20))

b1.place(x = 25, y = 120)
b7.place(x = 25, y =230)

b3 = tk.Button(root,width = 25, text ='Nearby Doctors', command = b3,font=('Courier', 20))

b4 = tk.Button(root,width = 25, text = 'Contact Developers', command = b4,font=('Courier', 20))

b3.place(x = 550, y = 120)
b4.place(x = 550, y =230)

b5 = tk.Button(root,width = 25, text ='Emergeny Alarm', command = b5,font=('Courier', 20), fg = 'white', bg = 'red')

b5.place(x = 287, y = 340)

b6 = tk.Button(root,width = 25, text ='Owner Control', command = b6 ,font=('Courier', 10), bg = 'grey')

b6.place(x = 750, y = 450)

b2 = tk.Button(root,width = 25, text ='Change Credentials', command = b2 ,font=('Courier', 10), bg = 'grey')

b2.place(x = 50, y = 450)

b8 = tk.Button(root,width = 25, text ='Patient Database', command = b8 ,font=('Courier', 10), bg = 'grey')

b8.place(x = 400,y = 450)

root.mainloop()


