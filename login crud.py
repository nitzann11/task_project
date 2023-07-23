from user_class import User
from files import save_data,load_data


def create_user(user:User):
    data=load_data(filename="accounts.pickle")
    data.append(user)
    save_data(filename="accounts.pickle",data=data)
        



    