import autodocdef as ad

#{'initiate': 0, 'id_use': None, 'pass': ''}

call1 = ad.readbin('ruleset.bin')
try:
    call2 = ad.readbin('v_ownerinfo.bin')
except:
    pass

if call1['initiate'] == 0:
    print("AutoDoc has not been setup yet.")
    i = input("Press Enter")

    print("Setting up the software: ")
    print()
    print("What entity do you represent?")
    print("1.Personal (i.e., for personal use)\n2.Private \n3.Government Entity\n4.Not specified here.\n")
    while True:
        ent = int(float(input("Enter code of entity: ")))
        if ent > 4 or ent < 1:
            print("Invalid code.\n")
        else:
            break
   
    if ent == 1:
        print("Welcome to AutoDoc Setup! \n")
        print("Terms of Service:\n")
        print(ad.readtxt("tac.txt"))
        print()
        i = input("Enter Y to agree to terms of service ")
        if i.upper() != 'Y':
            print("Thank you for your time.")
            print("Program will end in 5 seconds")
            ad.time.sleep(5)
            quit()
        print()
        while True:
            print("Enter User Name:")
            nam = input()
            if nam == '':
                print('Invalid; Try Again.')
            else:
                break
        print()
        print("Enter User Email ID")
        mail = input()
        ad.wribin("v_ownerinfo.bin", {'Name' : nam, 'Email' : mail}) 
        print()
        while True:
            print("Enter Preferred Username/ ID")
            use = input()
            if use == '':
                print('Invalid.')
            else:
                break
        print()
        print("Enter User Password: Carefully as you only have one trial")
        pas = input()
        print()
        ad.wribin("ruleset.bin", {'initiate': 1, 'id_use': use, 'pass': pas})
        print("AutoDoc has been setup!")
        ad.log("Setup for personal")
        ad.wricsv('v_pat.csv', ['id', 'name', 'contact email', 'user info initiated on'])
        ad.appcsv('v_pat.csv', [use, nam, mail, ad.time.ctime()])
        ad.log("PersonL Patient db initialized")
        ad.wribin('ruleset2.bin',{'ad_type':1})
        


    elif ent == 2:
        print("Welcome to AutoDoc Setup! \n")
        print("Terms of Service:\n")
        print(ad.readtxt("tac.txt"))
        print()
        i = input("Enter Y to agree to terms of service ")
        if i.upper() != 'Y':
            print("Thank you for your time.")
            print("Program will end in 5 seconds")
            ad.time.sleep(5)
            quit()
        print()
        while True:
            print("Enter Owner Name:")
            nam = input()
            if nam == '':
                print('Invalid.')
            else:
                break
        print()
        print("Enter Owner Email ID (for OPD department)")
        mail = input()
        ad.wribin("v_ownerinfo.bin", {'Name' : nam, 'Email' : mail}) 
        print()
        while True:
            print("Enter Preferred Username/ ID")
            use = input()
            if use == '':
                print('Invalid.')
            else:
                break
        print()
        print("Enter Owner Password: Carefully as you only have one trial")
        pas = input()
        print()
        ad.wribin("ruleset.bin", {'initiate': 1, 'id_use': use, 'pass': pas})
        print("AutoDoc has been setup!")
        ad.log("Setup for private")
        ad.wricsv('v_pat.csv', ['id', 'name', 'contact email', 'user info initiated on'])
        ad.appcsv('v_pat.csv', [use, nam, mail, ad.time.ctime()])
        ad.log("Patient db initialized")
        ad.wribin('ruleset2.bin',{'ad_type':2})

    elif ent== 3:
        print("Sorry, we have not yet been given authorization (or even noticed) by the govt.")
        i = input("Press enter to contact us instead for information about the program.")
        ad.webbrowser.open(r'https://docs.google.com/document/d/1HXdEAt5qQ859a5Nxou8PsIiE2l66tW_LyDUXgwlwBXM/edit?usp=sharing')
    else:
        print("Contact develpers to specify your needs")
        ad.webbrowser.open(r'https://docs.google.com/document/d/1HXdEAt5qQ859a5Nxou8PsIiE2l66tW_LyDUXgwlwBXM/edit?usp=sharing')
    ad.time.sleep(2)
    quit()
    


print()


print("Welcome to AutoDocCommand interface.\n")
for i in range(2):
    print("Enter passcode(Trials remaining " + str(2-i)+ ")")
    pass_call = input()
    if pass_call == call1['pass']:
        break
else:
    print("Invalid: Program will end in 5 seconds")
    ad.log("Invalid password at ad_command")
    ad.time.sleep(5)
    quit()

while True:
    
    print()

    print("Valid Actions:")

    act = ['1 - Input new user', '2 - Change Owner Passcode', '3 - Reset Interface', '4 - Delete user info']

    for i in act:
        print(i)

    print()


    while True:  
        act_call = int(float(input("Enter action code")))
        if act_call > len(act) or act_call<1:
            print("Invalid code")
        else:
            break

    act_code = act_call -1

    print()

    print("Performing action:", act[act_code])

    print()
    
    #1
    if act_call == 1:
        ad.log("New user entered")
        nam = input('Enter name: ')
        mail = input('Enter email id: ')
        use = input('Enter id: ')
        ad.appcsv('v_pat.csv', [use, nam, mail, ad.time.ctime()])

    #2
    if act_call == 2:
        print("Enter new password")
        i = input()
        ad.wribin("ruleset.bin", {'initiate': 1, 'id_use': None, 'pass': i})
        print("Password updated")
        ad.log("Password changed")
        

    #3
    if act_call == 3:
        print("Are you sure you want to RESET? Press Y")
        i = input()
        if i.upper() == 'Y':
            print("Reset in progress...")
            ad.reset()
            print("Reset done, program will end in 5 seconds")
            ad.log("Specs reset")
            ad.time.sleep(5)
            quit()

    #4
    if act_call == 4:
        use_del = input('Input id to be deleted')
        test = ad.idcheck(use_del)
        if test==True:
            
            #Program to create temp file
            ori = ad.readcsv('v_pat.csv')
            count = 0
            ad.wricsv('v_pat.csv', ['id', 'name', 'contact email', 'user info initiated on', 'last checkup', 'last diagnosis'])
            for i in ori:
                if count == 0:
                    count  = 1
                elif i[0] != use_del:
                    ad.appcsv('v_pat.csv', i)
                    
                else:
                    pass
            #End of program

                    
            ad.log('ID of '+  use_del +' deleted')
            print()
        else:
            print('ID does not exist')
            print()
            pass

    ad.quitcall()






