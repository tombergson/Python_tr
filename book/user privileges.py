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

class Admin(User):
  def __init__(self, first_name, last_name, age, gender, privileges):
    self.privileges = privileges
    super().__init__(first_name, last_name, age, gender)
  
  def show_privileges(self):
    print(f"Użytkownik {self.first_name.title()} {self.last_name.title()} może {self.privileges}")
  



user = Admin('tom', 'hillfinger', '21', 'mezczyzna', 'może dodać post')
user_1 = Admin('adam', 'kolski', '41', 'mezczyzna', 'może usunąć post')
user_2 = Admin('marek', 'leszcz', '45', 'mezczyzna', 'może banować')

for admin in [user, user_1, user_2]:
  print(f"\nUżytkownik: {admin.first_name.title()} {admin.last_name.title()}")
  print(f"  Wiek: {admin.age} lat")
  print(f"  Płeć: {admin.gender}")
  admin.greet_user()
  print(f"  Uprawnienia: {admin.privileges}")

