# Exercise: Save this code, run through mypy, understand the errors.
class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system

imran = Person("Imran", 22, "Ubuntu")
print(imran.name)
# print(imran.address)  # Bug: Person has no attribute 'address'
                        # mypy error: "Person" has no attribute "address"

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
# print(eliza.address)  # Bug: same error - Person has no attribute 'address'
                        # mypy error: "Person" has no attribute "address"
# Exercise: is_adult - mypy is happy because it knows Person has 'age'
def is_adult(person: Person) -> bool:
    return person.age >= 18
 
print(is_adult(imran))  # True
print(is_adult(eliza))  # True
 
# Exercise: function that accesses a property that doesn't exist
# mypy will catch this error before we even run the code
def get_address(person: Person) -> str:
    return person.address  # mypy error: "Person" has no attribute "address"