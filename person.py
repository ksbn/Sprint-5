import datetime
 
# Advantages of methods over free functions (written before looking at answers):
# 1. Easier to find - all Person behaviour is in one place
# 2. Encapsulation - if Person changes internally, only the class needs updating
# 3. Reads more naturally - imran.is_adult() vs is_adult(imran)
 
class Person:
    def __init__(self, name: str, date_of_birth: datetime.date, preferred_operating_system: str):
        self.name = name
        self.date_of_birth = date_of_birth  # changed from age: int
        self.preferred_operating_system = preferred_operating_system
 
    def is_adult(self) -> bool:
        today = datetime.date.today()
        age = today.year - self.date_of_birth.year
        # Adjust if birthday hasn't happened yet this year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age >= 18
 
imran = Person("Imran", datetime.date(2002, 5, 15), "Ubuntu")
print(imran.is_adult())  # True