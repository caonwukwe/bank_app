import random
import locale

from check import transfer
accounts = []
def bank_app():
    print("Welcome to Chyna's bank")
    main_menu = input("1. Register 2. Login: ")
    if(main_menu == "1"):
        register()
    elif(main_menu == "2"):
        login()


def register():
    firstname = input("Enter your firstname: ")
    lastname = input("Enter your lastname: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    email_exist = None
    for accout in accounts:
        if(accout["email"] == email):
            email_exist = True
            break
    if(email_exist is True):
        print("email already exist")
    else:
        account_number = random.randint(1000000000, 9999999999)
        
        amount = 50000
        new_user = {"firstname": firstname, "lastname": lastname, 
                "email": email, "password": password, "account": account_number, "amount": amount}
        accounts.append(new_user)
        print(accounts)
        print(f"Registration successful. Here is your account number {account_number} and your amount is {amount}")
        locale.setlocale(locale.LC_ALL, '')
        currency_string = locale.currency(50000, grouping= True)
        print(currency_string)



def login():
    email_or_account_num = input("Enter your email or account number: ")
    password = input("Enter your password: ")
    found_user = None
    for account in accounts:
        if(password == account["password"] and 
           (email_or_account_num == account["email"]) 
           or email_or_account_num == account["account"]):
            found_user = account
            print("login successful")
            break
    if(found_user is None):
        print("Inorrect login details supplied")

        bank_app()
        
    else:
        print(f"Your fullname is {found_user["firstname"]} {found_user["lastname"]} {found_user["amount"]}" )

        # bank_app()
        user_dashboard(found_user)
        


def user_dashboard(user):
    while True:

        print("1. to Transfer")
        print("2. to Check balance")
        print("3. to Logout")
        menu = input("choose an option: ")
        if(menu == "1"):
            transfer(user)
        elif(menu == "2"):
            print(f" your balance is {user["amount"]}")
        elif(menu == "3"):
            print("Logging out")
            bank_app()
            break
        else:
            print("Invalid option, you can try again")



def transfer_money(sender):
        receiver_account = input("Enter the account number of the receiver: ")
        
        receiver = None
        for account in accounts:
            if (account["account"]) == receiver_account:
                receiver_account == account
                break
            if(receiver is None):
                print("receiver account does not exist")
                return
            amount = input("Enter the amount you want to transfer: ")
            amount = int(amount)

            if(sender["amount"]) < amount:
                print("Insuffient balance")
            else:
                sender["amount"] == amount
                receiver["amount"] += amount
                print(f" Transfer successful! you have sent {amount} to {receiver["firstname"]} and {receiver["lastname"]}")
                bank_app()
        


bank_app()       