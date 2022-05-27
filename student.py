class Student:
    # name="Shirleen"
    # age=20
    # country="Kenya"
    # school="AkiraChix"
    # def __init__(self,name,age,country):
    #     self.name=name
    #     self.age=age
    #     self.country=country
    # def greet(self):
    #     return(f"Hello {self.name} you are {self.age} years old and you are from {self.school}")

    def __init__(self,name,name_initials):
        self.name=name
        self.name_initials=name_initials



   
    def full_name(self):
        return(f"Hello {self.name}")
    
    def year_of_birth(self,age):
        date_of_birth=2022-age
        return(f"Hello {self.name} you were born in {date_of_birth}")

    def initials(self):
        return(f"Hello your {self.name} use your name initial {self.name_initials}")


        





    
    
   

