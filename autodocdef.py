import csv
import webbrowser
import os
import pickle
import time
import playsound
from tkinter import messagebox
#Making definitions

def writxt(filename, data):
    with open(filename, 'w') as obj:
        obj.write(data)
        obj.close()

def wribin(filename, data):
    with open(filename, 'wb') as obj:
        pickle.dump(data, obj)
        obj.close()

def readtxt(filename):
    with open(filename, 'r') as obj:
        return obj.read()
        obj.close()

def readbin(filename):
    with open(filename, 'rb') as obj:
        return pickle.load(obj)
        obj.close()
        
def wricsv(filename, data):
    obj = open(filename, 'w', newline = '')
    cw = csv.writer(obj, delimiter = ',')
    cw.writerow(data)

def appcsv(filename, data):
    obj = open(filename, 'a', newline = '')
    cw = csv.writer(obj, delimiter = ',')
    cw.writerow(data)

def readcsv(filename):
    ret = []
    obj = open(filename, 'r', newline = '')
    cr = csv.reader(obj)
    for i in cr:
        ret.append(i)
    return ret
    

def quitcall():
    print("Press ENTER to CONTINUE \t OR \t input Q to QUIT Program:")
    i = input()
    if i=='':
        pass
    else:
        quit()

def reset():
    wribin("ruleset.bin", {'initiate': 0, 'id_use': None, 'pass': ''})
    try:
        os.remove('v_ownerinfo.bin')
    except:
        pass
    try:
        os.remove('v_pat.csv')
    except:
        pass
    try:
        os.remove('pat_hold.bin')
    except:
        pass
    
def log(s):
    with open('v_log.txt', 'a') as obj:
        obj.write(s + ' at ' + time.ctime() + '\n')
        obj.close()

def sound(file):
    playsound.playsound(file)

def idcheck(id_):
    if id_ == 'id':
        return False
    ret_list = readcsv('v_pat.csv')
    for i in ret_list:
        if i[0] == id_:
            return True
    else:
        return False

def pathold(id_):
    log('Pathold initiated for id' + id_)
    wribin('pat_hold.bin', [id_, time.ctime(), None])

def symp(l):
    if l == [0,0,0,0,0]:
        return 'Nothing'
    elif l == [0,0,0,0,1]:
        return 'Nausea'
    elif l == [0,0,0,1,0]:
        return 'Headache'
    elif l == [0,0,1,0,0]:
        return 'Difficulty in breathing'
    elif l == [0,1,0,0,0]:
        return 'Irregular heartbeat'
    elif l == [1,0,0,0,0]:
        return 'Fatigue'
#Individual lvl complete
    elif l == [0,0,0,1,1]:
        return 'Nausea,Headache'
    elif l == [0,0,1,0,1]:
        return 'Nausea,Difficulty in breathing'
    elif l == [0,1,0,0,1]:
        return 'Nausea,Irregular heartbeat'
    elif l == [1,0,0,0,1]:
        return 'Nausea,Fatigue'
    elif l == [0,0,1,1,0]:
        return 'Headache,Difficulty in breathing'
    elif l == [0,1,0,1,0]:
        return 'Headache,Irregular heartbeat'
    elif l == [1,0,0,1,0]:
        return 'Headache,Fatigue'
    elif l == [0,1,1,0,0]:
        return 'Difficulty in breathing,Irregular heartbeat'
    elif l == [1,0,1,0,0]:
        return 'Difficulty in breathing,Fatigue'
    elif l == [1,1,0,0,0]:
        return 'Irregular heartbeat,Fatigue'
#2nd degree over
    elif l == [0,0,1,1,1]:
        return 'Nausea,Headache,Difficulty in breathing'
    elif l == [0,1,0,1,1]:
        return 'Nausea,Headache,Irregular heartbeat'
    elif l == [1,0,0,1,1]:
        return 'Nausea,Headache,Fatigue'
    elif l == [0,1,1,0,1]:
        return 'Nausea,Difficulty in breathing,Irregular heartbeat'
    elif l == [1,0,1,0,1]:
        return 'Nausea,Difficulty in breathing,Fatigue'
    elif l == [1,1,0,0,1]:
        return 'Nausea,Irregular heartbeat,Fatigue'
    elif l == [0,1,1,1,0]:
        return 'Headache,Difficulty in breathing,Irregular heartbeat'
    elif l == [1,0,1,1,0]:
        return 'Headache,Difficulty in breathing,Fatigue'
    elif l == [1,1,0,1,0]:
        return 'Headache,Irregular heartbeat,Fatigue'
    elif l == [1,1,1,0,0]:
        return 'Difficulty in breathing,Irregular heartbeat,Fatigue'
#3rd degree over
    elif l == [0,1,1,1,1]:
        return 'Nausea,Headache,Difficulty in breathing,Irregular heartbeat'
    elif l == [1,0,1,1,1]:
        return 'Nausea,Headache,Difficulty in breathing,Fatigue'
    elif l == [1,1,0,1,1]:
        return 'Nausea,Headache,Irregular heartbeat,Fatigue'
    elif l == [1,1,1,0,1]:
        return 'Fatigue,Irregular heartbeat,Difficulty in breathing,Nausea'
    elif l == [1,1,1,1,0]:
        return 'Fatigue,Irregular heartbeat,Difficulty in breathing,Headache'
#4th degree over
    elif l == [1,1,1,1,1]:
        return 'Fatigue,Irregular heartbeat,Difficulty in breathing,Headache,Nausea'
    
    else:
        return 'Sorry unidentified disease error combo!'

def med(b):

        a=""
        if 'Nausea' in b:
            a=a+'For Nausea=Sleep\n'
        if 'Headache'in b:
            a=a+'For headache:Lots of sleep and rest,Head Massage\n'
        if 'Difficulty in breathing' in b:
            a=a+'For difficulty in breathing:2 puffs of Levolin inhaler/1 levolin capsule nebulization\n'
        if 'Irregular heartbeat' in b:
            a=a+'For irregular heartbeat:Calcium channel blocker,Antiarrhythmic drugs like-Ace inhibitors\n'
        if 'Fatigue' in b:
            a=a+'For fatigue:Reduce stress,Lots of sleep and rest\n'
        
        return a
    
