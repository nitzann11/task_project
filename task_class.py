from datetime import datetime,timedelta
class Task:
    #add day time
    def __init__(self,task_creator:str="undefined",task_name:str="undefined",creation_date:datetime=datetime.now(),deadline:datetime=datetime,time_diffrence:timedelta=timedelta()):

        self.task_creator=task_creator
        self.task_name=task_name
        self.creation_date=creation_date
        self.deadline=deadline
        self.time_diffrence=time_diffrence
        self.time_diffrence=timedelta(creation_date)
        
    def __str__(self) -> str:
        f'{self.task_creator}\t{self.task_name}\t{self.creation_date}\t{self.deadline}\t{self.time_diffrence}'
