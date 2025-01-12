class car:
   def __init__(self, color, brand, price, doors):
      self.color = color #red
      self.brand = brand
      self.price = price
      self.doors = doors

obj = car("red","bmw","12000",6)   # add value to above parameters

 
print(obj.brand)


#instance method = work with instance variable (keyword is self)
#satic method = dont work with others
#class method = work with class variable


class student:
   uni = "KMD"
   def __init__(self, name, year, age):
      self.name = name
      self.year = year
      self.age = age

      #static method
      def set_age(self,age):
         if age >= 15:
            self.age = age
         else:
            print("Invalid Age")
      
student_one = student("Aung","2023",23)
student_two = student("Bo","2023",24)

student.uni = "MIT"  # changing or overwriting uni value

print(student_one.uni)
print(student_two.uni)  
#can call class value from object of its class

student_one.set_age(2)
print(student_one.set_age)



class person:
   def __init__(self, name,age,id):
      self.__name = name 
      self.__age = age 
      self.__id = id       # __ means the private 

   def get_name(self):  # this is public interface
      return self.__name
   
   def get_id(self):
      return self.__id

   def get_age(self):
      return self.__age

   def set_age(self,age):   #dont forget the parameter in the setter method.
      #self.__age = age
      if age > 70 or age <= 0:
         print("Your age is Invalid!")
      else:
         self.__age = age
      

first = person("Ki",21,1211)
name = first.get_name()
print(name)

first_id = first.get_id()
print(first_id)

age = first.get_age()
print(age)

first.set_age(100)
age = first.get_age()
print(age)



# specail methods
#__init__
#__str__   use when you want to cut the specific parts in printing
#__len__   use when you want to find length for object
#__dir__  use to abstract the attributes which can be used behind the object
#__eq__  use when you want to test the condition(equal or not)for objects(checking their values in them not address)

class book:
   def __init__(self,name,pages,year):
      self.name = name
      self.pages = pages
      self.year = year

   def __str__(self):  #__str__   use when you want to cut the specific parts in printing
      return f"The book 1 : {self.name}"

   def __len__(self):   #__len__   use when you want to find length for object
      return self.pages

   def __eq__(self,others):  # need to add second variable to receive the value
      if self.name == others.name and self.year == others.year:
         return True
      else:
         return False

   # creating a method
   def display_info(self):
      print(f"{self.name}{self.pages}{self.year}")

book1 = book("All trust in God",200,1998)
book2 = book("All trust in God",450,1998)
print(book1)
print(len(book1))

# creating a variable for getting avlue for dir
value_from_dir = book1. __dir__()
print(type(value_from_dir))
print(value_from_dir)

print(id(book1))
print(id(book2))

print(book1 == book2)
