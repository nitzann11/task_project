from files import save_data,load_data
from task_class import Task
from datetime import datetime,timedelta

def create_task(task=Task):
    data=load_data()
    data.append(task)
    save_data(data=data)
    print("task created.")

def view_tasks(parameter:str="1",name:str="",task_name:str="",category:str=""):
    data=load_data()
    for task in data:
        if parameter=="1":
            print(task)
        elif parameter=="2":
            if task.name==name:
                print(task)
        elif parameter=="3":
            if task.task_name==task_name:
                print(task)
        elif parameter=="4":
            if task.category==category:
                print(task)



def update_task(name:str="",task_name:str="",parameter:str="",value:str="",date_value:datetime=datetime(year=2023,month=1,day=1)):
    data=load_data()
    for task in data:
        if task.name==name and task_name==task_name:
            if parameter=="1":
                task.name==value
            elif parameter=="2":
                task.task_name==value
            elif parameter=="3":
                task.category==value
            elif parameter=="4":
                task.deadline==date_value
            elif parameter=="5":
                task.time_diffrence==timedelta(task.creation_date,task.deadline)
            save_data(data=data)
            print("task has been updated")

def delete_task(name,task_name):
    data=load_data()
    for task in data:
        if task.name==name and task_name==task_name:
            data.remove(task)
            save_data(data=data) 
            print("task deleted.")
        else:
            print("task wasn't found.")
               

    
    

    
    