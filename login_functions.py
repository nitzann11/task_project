from user_class import User
from files import save_data,load_data

def login(username:str="",password:str=""):
    data=load_data(filename="accounts.pickle")
    for user in data:
        if user.username==username and user.password==password:
            return f"Welcome {user.name}!"
        else:
            return 'Wrong cradentials please try again' 


def create_user(user:User):
    data=load_data(filename="accounts.pickle")
    data.append(user)
    save_data(filename="accounts.pickle",data=data)
    
def forgot_password(username:str="",email:str="",new_password:str=""):
    data=load_data(filename="accounts.pickle")
    for user in data:
            if user.username==username and user.email==email:
                user.password==new_password
                try:
                    save_data(filename="accounts.pickle",data=data)
                except:
                    print("something went wrong")
            else:
                print("wrong cradentials,try again")
    
def change_status(username:str="",password:str=""):
    data=load_data("accounts.pickle")
    for user in data:
        if user.username==username and user.password==password and user.status=="active":
            user.status=="disabled"
        elif user.username==username and user.password==password and user.status=="disabled":
            user.status=="enabled"
    save_data(filename="accounts.pickle",data=data)            
        

        



    