import autodocdef as ad
import tkinter as tk
from tkinter import Checkbutton
from tkinter import messagebox
#Check-up window


    
root = tk.Tk()

try:
    id_ = ad.readbin('pat_hold.bin')
except:
    messagebox.showinfo('No ID given.')
    root.destroy()
    ad.os.system('AutoDoc.py')
    quit()

root.geometry('800x600')

root.title('AutoDoc - Checkup')

label_head = tk.Label(root, text = 'AutoDoc', font=('Courier', 25))

label_head.pack()

label_sub = tk.Label(root, text = 'Select Relevant Symptoms', font=('Courier', 20))

label_sub.pack()

#Symps

def get_value():
    l = []
    for c in (c1,c2,c3,c4,c5):
        a = c.get()
        if a == False:
            l.append(0)
        else:
            l.append(1)
    diag = ad.symp(l)
    if diag != 'na':
        
        messagebox.showinfo('AutoDoc', 'You have been diagnosed with ' +diag)
        id_[2] = diag
        ad.wribin('pat_hold.bin', id_)
        ad.log('Logged ' + str(id_))
        if l ==[0,0,0,0,0]:
            call = messagebox.askyesno('AutoDoc', 'Press yes to enter symptoms again, or no to end application')
            if call == False:
                quit()
            else:
                root.destroy()
                ad.os.system('ad_checkup.py')
        else:
            root.destroy()
            ad.os.system('ad_sympdisplay.py')
    else:
        ad.log('Diagnosis of combiantion ' + str(l) + ' failed')
        messagebox.showinfo('AutoDoc', 'Diagnosis failed; Please update owner.')
        call = messagebox.askyesno('AutoDoc', 'Press yes to enter symptoms again, or no to end application')
        if call == False:
            quit()
        else:
            root.destroy()
            ad.os.system('ad_checkup.py')
c1=tk.BooleanVar()
c2=tk.BooleanVar()
c3=tk.BooleanVar()
c4=tk.BooleanVar()
c5=tk.BooleanVar()

s1 = Checkbutton(root, text ='Fatigue',variable=c1
                   ,font=('Courier', 18)).place(x = 30, y = 100)

s2 = Checkbutton(root, text ='Irregular Heartbeat',variable=c2,
                  font=('Courier', 18)).place(x = 30, y = 140)
  
s3 = Checkbutton(root, text ='Difficulty in Breathing',variable=c3,
                     font=('Courier', 18)).place(x = 30, y = 180)
  
s4 = Checkbutton(root, text ='Headache',variable=c4, 
                font=('Courier', 18)).place(x = 30, y = 220)

s5 = Checkbutton(root, text ='Nausea',variable=c5, 
                font=('Courier', 18)).place(x = 30, y = 260)

l_place = tk.Label(root, text = ' ').pack(side = 'bottom')
b_out = tk.Button(root, text = 'Continue', font=('Courier', 20), bg = 'grey', command = get_value).pack(side = 'bottom')



#End of symps

root.mainloop()
