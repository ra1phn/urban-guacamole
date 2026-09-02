"""
Object oriented programming
<JS, Python, C++, JAVA, etc>
------------------------------------------
Concept in programming to make work easy by
using principles
1. Encapsulation
    -keeping data and methods<functions> inside a class
    while restricting direct access to internal data. 
2. Abstraction
    -Hiding unnecessary complexity or implrtation of details
3. Inheritance
    -one clas to reuse or extend properties 
    and methods of another class
4. Polymorphisim
    -Appearing in different forms. method can
    have different behaviours.
_________________________________________________________________

JS and Python are object oriented. 
-- number.toString(), string.toLowerCase()

"""

"""
--CLASS--
- it is a blueprint for an object. 

-class would be an architectural drawing of a house.
-object would be implimentation of the drawing

"""

#is to have the name capitalized

class House:
    bedrooms=3
    bathrooms=2
    floors=1
    area=120
    owner=""
    location=""
    architect="KIMANI"

    def __init__(self, owner, location):
        print("Class house created. initializer called")
        self.owner=owner
        self.location=location

    def config(self, owner, location):
        print("config method has run")
        self.owner=owner
        self.location=location


    def print_self(self):
        #this <the object itself>: self<object>
        print(self)
        print(self.__dict__) # dictionary (prints all items)

# When accessing object properties use dot notation
# Bracket notaiton is for dictionary

# -method.config 
# - print self
# instance class --> create an object from a class
ralph_house=House(owner="Ralph",location="Kikuyu")
# ralph_house.__init__()
# ralph_house.owner="Ralph"
# ralph_house.location="Kikuyu"
print(f"Ralph's house owner {ralph_house.owner}")
print(f"Ralph's house location {ralph_house.location}")
print(f"Ralph's house bedrooms {ralph_house.bedrooms}")
print(f"Ralph's house bathrooms {ralph_house.bathrooms}")
print(f"Ralph's house floors {ralph_house.floors}")
print(f"Ralph's house area {ralph_house.area}")
print(f"Ralph's house architect {ralph_house.architect}")
print("Printing Ralph's house")
ralph_house.print_self()
print("End or printing Ralph's house")




print("----------------------------------------------------")

daniel_house=House(owner="Daniel", location="Muranga") #__init__()
# daniel_house.owner="Daniel"
# daniel_house.location="Muranga"
# daniel_house.config(owner="Daniel", location="Muranga")
print(f"Daniel's house owner {daniel_house.owner}")
print(f"Daniel's house location {daniel_house.location}")
print(f"Daniel's house bedrooms {daniel_house.bedrooms}")
print(f"Daniel's house bathrooms {daniel_house.bathrooms}")
print(f"Daniel's house floor {daniel_house.floors}")
print(f"Daniel's house area {daniel_house.area}")
print(f"Daniel's house architect {daniel_house.architect}")
print("Printing Daniel's house")
daniel_house.print_self()
print("End or printing Daniel's house")
