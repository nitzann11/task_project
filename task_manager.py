from app import main_menu
from crud import create_task,view_tasks,update_task,delete_task
from task_class import Task
from datetime import datetime

def tasks_manager():
    while True:
        print("""
        Tasks manager:
        1.create a new task
        2.view tasks
        3.update existing task
        4.delete a task
        5.return to main menu""")
        options=["1","2","3","4","5"]
        action=str(input("choose action 1-5: "))

        if action in options:
            if action=="1":
                name=str(input("task owner: "))
                task_name=str(input("task name: "))
                category=str(input("task category: "))
                deadline=datetime(year=input("enter year"),month=input("enter month:"),day=input("enter day"))
                create_task(Task(name,task_name,category,deadline=deadline))
                print("task has been added")
            
            elif action=="2":
                view_options=["1","2","3","4"]
                print("""
                view by:
                      1.view all
                      2.view by task owner
                      3.view by task name
                      4.view by category""")
                view_action=str(input("choose filter: "))
                while view_action not in view_options:
                    print("""
                    wrong input.. try again
                    view by:
                      1.view all
                      2.view by task owner
                      3.view by task name
                      4.view by category""")
                    view_action=str(input("choose filter: "))
                    
                view_tasks(view_action)
            
            elif action=="3":
                update_options=["1","2","3","4","5"]
                print("""
                task update menu:
                 1.update task owner
                 2.update task name
                 3.update task category
                 4.update task deadline
                 5.update remaining time
                """)
                update_action=str(input("choose action 1-5: "))
                while update_action not in options:
                    print("""
                    wrong input.. try again
                    task update menu:
                    1.update task owner
                    2.update task name
                    3.update task category
                    4.update task deadline
                    5.update remaining time
                    """)
                    update_action=str(input("choose action 1-5: "))
                update_task(update_action)
            
            elif action=="4":
                del_name=str(input("specify task owner: "))
                del_task_name=str(input("specify task name: "))
                delete_task(del_name,del_task_name)
            
            elif action=="5":
                main_menu()
                    
                    
                
                

