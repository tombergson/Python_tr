class User:
     
    def __init__(self, first_name, last_name, age, gender):
         
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
       
    
    def describe_user(self):
       
        print(f"Użytkownik nazywa się {self.first_name.title()} {self.last_name.title()}. Ma {self.age} lat i jest {self.gender}. ")


    def greet_user(self):
       
        print(f"Witaj {self.first_name.title()} {self.last_name.title()} ! ")


user = User('tom', 'hillfinger', '21', 'mezczyzna')
user_1 = User('adam', 'kolski', '41', 'mezczyzna')
user_2 = User('marek', 'leszcz', '45', 'mezczyzna')

for admin in [user, user_1, user_2]:
  print(f"\nUżytkownik: {admin.first_name.title()} {admin.last_name.title()}")
  print(f"  Wiek: {admin.age} lat")
  print(f"  Płeć: {admin.gender}")
  admin.greet_user()
 