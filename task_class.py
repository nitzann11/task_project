from datetime import datetime,timedelta
class Task:
    #add day time
    def __init__(self,task_creator:str="undefined",task_name:str="undefined",category:str="undefined",creation_date:datetime=datetime.now(),deadline:datetime=datetime.today()):

        self.task_creator=task_creator
        self.task_name=task_name
        self.category=category
        self.creation_date=creation_date
        self.deadline=deadline
        self.time_diffrence=timedelta(creation_date,deadline)
        
    def __str__(self) -> str:
        f'{self.task_creator}\t{self.task_name}\t{self.category}\t{self.creation_date}\t{self.deadline}\t{self.time_diffrence}'
