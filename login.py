from login_functions import create_user,login,forgot_password
from user_class import User
def login_menu():
    while True:
        print("""
        Login menu:
        1.Log in
        2.Create a new account
        3.Forgot password
        4.exit""")

        options=["1","2","3","4"]
        action=input("choose option:1-4")
        if action in options:
            if action=="1":
                login_username=input("Enter Username: ")
                login_password=input("Enter password: ")
                login(login_username,login_password)
            elif action =="2":
                new_name=input("enter your name: ")
                new_username=input("enter your username: ")
                new_password=input("enter your password: ")
                new_email=input("enter your email: ")
                create_user(User(name=new_name,username=new_username,password=new_password,email=new_email))
            elif action =="3":
                username_check=input("enter account username: ")
                email_check=input("enter account username: ")
                renew_password=input("enter the new password:" )
                forgot_password(username=username_check,email=email_check,new_password=renew_password)    
                
            elif action=="4":
                exit()
        else:
            print("invalid action, try again..")
