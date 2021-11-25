import autodocdef as ad

import tkinter as tk

from tkinter import messagebox

root = tk.Tk()

root.title('AutoDoc - Complementary Health Checkup')

root.geometry('500x300')

lab_top = tk.Label(root, text = 'AutoDoc', font = ('courier', 20)).pack()

lab_place = tk.Label(root, text = ' ', font =('courier', 10)).pack()

def get_val():
    weight = float(e_weight.get())
    age = float(e_age.get())
    bpm = int(e_bpm.get())
    height = float(e_height.get())
    #Conditions:

    bmi = weight/((height)**2)
    bmi = round(bmi, 2)

    if bmi<18.5:
        bmi_c = 'A bmi of '+ str(bmi) + ' indicates that you are underweight '
    elif bmi>25:
        bmi_c = 'A bmi of '+ str(bmi) + ' indicates that you are overweight '
    else:
        bmi_c = 'A bmi of '+ str(bmi) + ' indicates that you are normal '
        

    if age <16:
        if bpm > 60 and bpm < 100:
            bpm_c = 'and a bpm of ' + str(bpm) + ' is relatively okay.'
        else:
            bpm_c = 'and a bpm of ' + str(bpm) + ' is not usual. Consult a medical practioner.'
    else:
        if bpm > 70 and bpm < 105:
            bpm_c = 'and a bpm of ' + str(bpm) + ' is relatively okay.'
        else:
            bpm_c = 'and a bpm of ' + str(bpm) + ' is not usual. Consult a medical practioner.'
    st = bmi_c + bpm_c
    tk.messagebox.showinfo('AutoDoc', st)
    
    

lab_txt = tk.Label(root, text = 'Enter Weight in kilogram', font = ('courier', 12)).place(x = 20, y = 40)
e_weight = tk.Entry(root, font = ('Arial', 10))
e_weight.place(x = 300, y = 43)


lab_txt = tk.Label(root, text = 'Enter Age in years', font = ('courier', 12)).place(x = 20, y = 80)
e_age = tk.Entry(root, font = ('Arial', 10))
e_age.place(x = 300, y = 83)

lab_txt = tk.Label(root, text = 'Enter Height in metre', font = ('courier', 12)).place(x = 20, y = 120)
e_height = tk.Entry(root, font = ('Arial', 10))
e_height.place(x = 300, y = 123)

lab_txt = tk.Label(root, text = 'Enter Beats Per Minute', font = ('courier', 12)).place(x = 20, y = 160)
e_bpm = tk.Entry(root, font = ('Arial', 10))
e_bpm.place(x = 300, y = 163)

lab_place = tk.Label(root, text = ' ', font =('courier', 10)).pack(side = 'bottom')

but = tk.Button(root, text = 'Check you health!', font = ('courier', 12), command = get_val)
but.pack(side = 'bottom')
root.mainloop()
