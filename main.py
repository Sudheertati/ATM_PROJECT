import random
import  Account_details as ad
import userdetails as ud
import Transaction_Process as tp

'''ATM Machine (Store User Data’s in a json file, 
Create Account, Create User, 
Credit/Debit, 
View Transaction history, 
Update user details, 
20 rupees charged after 3 withdraws in a month)'''
      
object1=ad.Account_Creation()
object2=ud.User_Creation()
object3=tp.Transaction()

while True :
    print('1.create user')
    print('2.create account')
    print('3.credit option')
    print('4.Debit option')
    print('5.View Transaction history')
    print('6.update details')

    try:
        choice=input("Enter the option : ")
    except Exception as e:
        print(e)
    if choice=='1':
        empid=random.randint(10000,100000)
        object2.Create_User(empid)
        print("Employee id is :",empid)
    elif choice=='2' :     
        object1.account_create()       
    elif choice =='3' :
        object3.credit()
    elif choice =='4':
        object3.debit()
    elif choice=='5':
        object3.Transaction_history()
    elif choice == '6':        
        print('1.Update for user details')
        print('2.Update for Account Details')
        temp1=int(input(' Enter choice :'))        
        if temp1==1:
            temp=input("Enter Employee id  to user account update")
            object2.User_details_Update(temp)
        elif temp1==2:
            temp=input("Enter Employee id number to Account details update")
            object1.Account_details_Update(temp)
            pass
    else :
        temp=input("you may  want to leave , if yes means press 1 or else press enter:")
        if temp =='1':
            break
            
        else :
            pass
                        
    print('-'*113)