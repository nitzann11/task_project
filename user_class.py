class User:
    def __init__(self,name:str="undefined",username:str="undefined",password:str="undefined",email:str="undefined",status:str="active"):
        self.name=name
        self.username=username
        self.password=password
        self.email=email
        self.status=status

    def __str__(self) -> str:
        f'{self.name}\t{self.username}\t{self.password}\t{self.email}\t{self.status}'

