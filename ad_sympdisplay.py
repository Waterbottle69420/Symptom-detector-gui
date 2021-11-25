import autodocdef as ad

import tkinter as tk

try:
    id_ = ad.readbin('pat_hold.bin')
except:
    messagebox.showinfo('No ID given.')
    ad.os.system('AutoDoc.py')
    

def home():
    root.destroy()
    
    ori = ad.readcsv('v_pat.csv')
    count = 0
    ad.wricsv('v_pat.csv', ['id', 'name', 'contact email', 'user info initiated on'])
    for i in ori:
        if count == 0:
            count  = 1
        elif i[0] != id_[0]:
            ad.appcsv('v_pat.csv', i)   
        else:
            i[4] = ad.time.ctime()
            i[5] = id_[2]
            ad.appcsv('v_pat.csv', i)
    ad.os.system('AutoDoc.py')

root = tk.Tk()

root.title('AutoDoc')

root.geometry('900x500')

label_head = tk.Label(root, text = 'AutoDoc', font=('Courier', 25))

label_head.pack()

label_sub = tk.Label(root, text = 'Kindly use these medications:\n', font=('Courier', 20))

label_sub.pack()

label_sub = tk.Label(root, text = ad.med(id_[2]), font=('Courier', 15))

label_sub.pack()

label_disclaimer = tk.Label(root, text = 'interface(yet), and thus, shall not be liable for any damage, personal, or otherwise.', font=('Courier', 5)).pack(side = 'bottom')

label_disclaimer = tk.Label(root, text = 'We do not take responsibility for the efficacy of said', font=('Courier', 5)).pack(side = 'bottom')

label_disclaimer = tk.Label(root, text = 'Consulation of a physician is always preferred.', font=('Courier', 8)).pack(side = 'bottom')

label_disclaimer = tk.Label(root, text = '\n', font=('Courier', 8)).pack(side = 'bottom')


b1 = tk.Button(root, text = 'Home Page', font=('Courier', 15), command = home).pack(side = 'bottom')
root.mainloop()
