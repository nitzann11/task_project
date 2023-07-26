from files import save_data,load_data
from task_class import Task

def create_task(task=Task):
    data=load_data()
    data.append(task)
    save_data(data=data)

def view_all(): 
    data=load_data()
    for task in data:
        print(task)

def view_by_user(name):
    data=load_data()
    for task in data:
        if task.name==name:
            print(task)    
    