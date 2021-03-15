from ed_gym import data_store

gym = data_store.Gym_Member()


while True:
    print('\nWelcome to Edyoda Gym!!!\n\n1. Super User login\n2. User login\n3. Exit\n')
    choose = input("Enter option number:\t")
    if choose == '1':
        while True:
            print("\n\n####################################\n")
            print("Welcome to Super User Login page")
            ad_username = input("Enter your username:\t")
            ad_pass = input("Enter your password:\t")
            if  ad_username not in gym.admin:
                print("please enter valid username and password")
            else:
                while True:
                   if gym.admin[ad_username] == ad_pass:
                        
                        while True:
                            print("\n####################################\n")
                            print("Hello Super User\n\nMain Menu:")
                            print("1. Create Member\n2. View Member\n3. Delete Member\n4. Update Member\n5. Create Regimen\n6. View Regimen\n7. Delete Regimen\n8. Update Regimen\n0. Logout")
                            a = input("Enter the option number:\t")
                            if a == "1":
                                gym.add_mem()
                            
                            elif a =='2':
                                while True:
                                    um = input("Enter Membership ID:\t")
                                    if um in gym.details:
                                        for i in gym.details[um]:
                                            print(i,'-',gym.details[um][i])
                                        print("\n###### Diverting to Main Menu ######\n")
                                        break
                                    else:
                                        print("please enter valid membership id")
                                                            
                            elif a =='3':
                                while True:
                                    dm = input("Enter Membership ID for deleting user details permanently:\t")
                                    if dm in gym.details:
                                        gym.details.pop(dm)
                                        print("\nDetails of Membership ID -", dm, "is deleted permanently\n\n###### Diverting to Main Menu ######")
                                        break
                                    else:
                                        print("Please enter valid member id")
                            elif a == '4':
                                while True:
                                    um = input("Enter Membership ID for updating details:\t")
                                    if um in gym.details:
                                        num = 0
                                        for i in gym.details[um]:
                                            print(str(num)+'.',i,'-',gym.details[um][i])
                                            num+=1
                                        print('9. Back')
                                        while True:
                                            c = input("Enter the option number (between 1 to 9): ")
                                            if c == '1':
                                                new = input("Enter name: ")
                                                gym.details[um]['Name'] = new
                                            elif c == '2':
                                                new = input("Enter age: ")
                                                gym.details[um]['Age'] = new
                                            elif c == '3':
                                                new = input("Enter Gender: ")
                                                gym.details[um]['Gender'] = new
                                            elif c == '4':
                                                new = input("Enter Mobile Number: ")
                                                gym.details[um]['Mobile Number'] = new  
                                            elif c == '5':
                                                new = input("Enter Email: ")
                                                gym.details[um]['Email'] = new 
                                            elif c == '6':
                                                w = float(input('Enter weight (in Kg): '))
                                                h = float(input('Enter height (in M) [for eg; 1.40,1.64,etc.]: '))
                                                gym.details[um]['BMI'] = w/(h * h)
                                            elif c == '7':
                                                new = input("Enter Membership Duration(in Months (1, 3, 6, or 12)): ")
                                                gym.details[um]['Membership Duration(Months)'] = new
                                            elif c == '8':
                                                new = input("Enter new status: ")
                                                gym.details[um]['Status'] = new
                                            elif c == '0':
                                                print("\nMembership ID cannot be modified")
                                            elif c == '9':
                                                print("\n###### Diverting to Main Menu ######\n")
                                                break
                                            else:
                                                print("\nPlease enter valid option")
                                        break
                                    else:
                                        print("\nEnter valid Membership ID\n")
                            
                            elif a == '5':
                                while True:
                                    id = input('Enter Membership ID for you want to create:\t')
                                    if id in gym.details:
                                        gym.regi(id)
                                        num = 1
                                        print("\nRegimen created:")
                                        for i in gym.regimen[id]:
                                            print(str(num)+'.',i,'-',gym.regimen[id][i])
                                            num+=1
                                        print("\n###### Diverting to Main Menu ######\n")
                                        break
                                    else:
                                        print("Please enter valid Membership ID")
                            
                            elif a == '6':
                                while True:
                                    id = input('Enter Membership ID for you want to view:\t')
                                    if id in gym.regimen and id in gym.details:
                                        num = 1
                                        for i in gym.regimen[id]:
                                                print(str(num)+'.', i, '-', gym.regimen[id][i])
                                                num+=1
                                        print("\n###### Diverting to Main Menu ######\n")
                                        break
                                    elif id not in gym.regimen and id in gym.details:
                                        print("Regimen is not created for this ID\nCreate the regimen for the member")
                                        print("\n###### Diverting to Main Menu ######\n")
                                        break
                                    else:
                                        print("Please enter valid Membership ID")
                            elif a == "7":
                                while True:
                                    did= input('Enter Membership ID: ')
                                    if did in gym.details and did in gym.regimen:
                                        gym.regimen.pop(did)
                                        print('\nRegimen for ID',did,'id deleted permanently\n\n')
                                        print("\n###### Diverting to Main Menu ######\n")
                                        break
                                    else:
                                        print("Regime is not present for the given ID")
                            elif a == '8':
                                while True:
                                    um = input("Enter Membership ID for updating regimen:\t")
                                    if um not in gym.regimen and um in gym.details:
                                        print("Regime not created for id", um)
                                        print("\n###### Diverting to Main Menu ######\n")
                                        break
                                    elif um in gym.regimen:
                                        num = 1
                                        print("")
                                        for i in gym.regimen[um]:
                                            print(str(num)+'.',i,'-',gym.regimen[um][i])
                                            num+=1
                                        print('0. Back')
                                        while True:
                                            c = input("Enter the option number:\t")
                                            if c == '1':
                                                new = input("Enter regimen for Mon: ")
                                                gym.regimen[um]['Mon'] = new
                                            elif c == '2':
                                                new = input("Enter Tue: ")
                                                gym.regimen[um]['Tue'] = new
                                            elif c == '3':
                                                new = input("Enter regimen for Wed: ")
                                                gym.regimen[um]['Wed'] = new
                                            elif c == '4':
                                                new = input("Enter regimen for Thu: ")
                                                gym.regimen[um]['Thu'] = new  
                                            elif c == '5':
                                                new = input("Enter regimen for Fri: ")
                                                gym.regimen[um]['Fri'] = new 
                                            elif c == '6':
                                                new = input("Enter regimen for Sat: ")
                                                gym.regimen[um]['Sat'] = new 
                                            elif c == '7':
                                                new = input("Enter regimen for Sun: ")
                                                gym.regimen[um]['Sun'] = new 
                                            elif c == '0':
                                                print("\n###### Diverting to Main Menu ######\n")
                                                break
                                            else:
                                                print("\nPlease enter valid option")
                                        break
                                    else:
                                        print("\nEnter valid Membership ID\n")
                                            
                            elif a == '0':
                                print("##### Logging out #####")
                                break
                            
                            else:
                                print("Please enter valid option")
                        
                   break
                else:
                    print("Please Enter valid username or password")
                break
    elif choose == '2':
        while True:
            print("\n\n####################################\n")
            print("Welcome to User Login page")
            ad_username = input("Enter your username:\t")
            ad_pass = input("Enter your password:\t")
            if  ad_username not in gym.user :
                print("please enter valid username and password")
            else:
                while True:
                   if gym.user[ad_username] == ad_pass:
                       while True:
                           print("\n####################################\n")
                           print("Hello",gym.details[ad_username]["Name"],"\nMain Menu:")
                           print("1. My Regimen\n2. My Profile\n3. logout")
                           c = input("Enter the option number:\t")
                           if c == '1':
                               if ad_username not in gym.regimen:
                                   print("Your regimen is not created yet!!\nPlease contact the Super User.\n\nThank you!")
                               else:
                                   for i in gym.regimen[ad_username]:
                                       print(i,'-',gym.regimen[ad_username][i])
                                   print("\n###### Diverting to Main Menu ######\n")
                           elif c =='2':
                               for i in gym.details[ad_username]:
                                   print(i,"-",gym.details[ad_username][i])
                               print("\n###### Diverting to Main Menu ######\n")
                           elif c =='3':
                               print("##### Logging out #####")
                               break
                           else:
                               print("PLease enter valid option number")
                       break
                   else:
                       print("please enter valid username and password")
            break
    elif choose == '3':
        print("###### Exiting ######")
        break
    else:
        print("please enter valid opion")
        
        
        
        
