# Magic Methods
# dir(examples : str or len or int or float) ما بها من magic methods => print(dir(name of method))
# __init__ => انشاء نموذج اساسي لاي شيء يؤخذ منه لعمل العديد من النسخ => def__init__(self):
# __class__ => معرفة اي كلاس ينتمي اليه المتغير ده => print(variable.__class__)
# __str__ => عندما تطبع الكلاس زي ما هو من غير اما تنادي اي حاجه جواه يعطك كلام غير مفهوم اما عندما تستعمل هذه يطبعلك ما تحتها من غير مناداتها => def__str__(self):
# __len__ => عندما تسأل عن طول عناصر ال __init__ بدونه باستخدام len(class_name) لا يعطيك شيء ولكن عند استعماله يعطك طول اللي جوا __init__ => def__len__(self):

# .mro() => الطريق اللي مشيت فيه البايثون لتعطي النواتج وتستعمل اكتر من الكلاس => print(class_name.mro())
# Polymorphism (تعدد الاوجه) => اي ان الميثود الواحدة تعمل اكثر من عمل مختلف عندما يتغير مكانها وتستعمل في الكلاس على ان الفانكيشن الواحده موجوده في اكثر من كلاس وفي كل كلاس بتعمل عمل مختلف => Methods like len(), +, -, & others
# raise => عمل خطأ => raise Error("Error")
# NotImplementedError => استكشاف هل الناتج من الكلاس ام لا => raise NotImplementedError("Something")

# Encapsulation
# 1. Public => تقدر تتصرف في المتغير اللي من النوع ده من جوا الكلاس او من جوا الكلاس الوارثين او من اي مكان في الكود => def __init__(self, name)
# 2. Protected => تقدر تتصرف في المتغير اللي من النوع ده من جوا الكلاس او من جوا الكلاس الوارثين فقط وتتميز باشارة (_) قبل اسم المتغير => def __init__(self, _name)
# 3. Protected => تقدر تتصرف في المتغير اللي من النوع ده من جوا الكلاس او من جوا الكلاس الوارثين فقط وتتميز باشارة (__) قبل اسم المتغير => def __init__(self, __name)
# اسم المتغير => def __init__(self, name) => name is variable
# Attribute = Variable here

# Getter & Setter in Private Attributes
# 1. Getter is a function that give me a private attribute without go in class => Example => class A: => def __init(self, __name): pass => def get_name(self): => return self.__name  =>  print(A("private name").get_name())
# 2. Setter is a function that change a private attribute without go in class => Example => class A: => def __init(self, __name): pass => def get_name(self, new_name): => self.__name = new_name  =>  A("private name").set_name("new name")


# Property
# 1. @property + method without () = method with ()
# 2. @property + method with () = Error
# 3. method without () = Informations of method in class


# Abstractmethod (ABCs) => جعل الفانكيشن اللي تحتوي علي هذه الخاصية في الكلاس الاصلي نموذج يمشي عليه نفس الفانكيشن الموجوده في الكلاس الوارثين فيبقى الكلاس الاصلي يحتوي على فانكيشن بدون اجابة والوارثين يحتوي على نفس الفانكيشن ولكن باجابات تناسبهم => from abc import abstractmethod => class Name: => @abstractmethod => function name with (pass) only







# __class__

print("__class__")
class User:
    def __init__(self):
        self.name = "Basel"
    
user_name = User()
print(user_name.__class__)
print(type(user_name))

print("-" * 50)








# __str__
print("__str__")
class User:
    def __init__(self):
        self.name = "Basel"
    
user_name = User()
print(user_name)


print("-" * 50)


class User:
    def __init__(self):
        self.name = "Basel"
    def __str__(self):
        return(f"My name is {self.name}")
    
user_name = User()
print(user_name)

print("-" * 50)


class User1(User):
    pass
    
user_name = User()
print(user_name)










# __len__
print("__len__")
class User:
    def __init__(self):
        self.name = "Basel"
    
user_name = User()
print(len(user_name))

print("-" * 50)

class User:
    def __init__(self):
        self.name = "Basel"
    def __len__(self):
        return len(self.name)
    
user_name = User()
print(len(user_name))




print("-" * 50)



# Polymorphism (تعدد الاوجه)
# 1- Methods
# +
n1 = 5
n2 = 10
print(n1 + n2) # 15

s1 = "Hello"
s2 = "Python"
print(s1 + " " + s2) # Hello Python

print("-" * 50)


# len()
print(len([1,2,3,4,5,6])) # 6
print(len({"key_one": 5, "key_two": 10})) # 2
print(len("Basel Salman")) # 12

print("-" * 50)



# 2- Classes
class A:
    def do_something():
        print("From class A") # A.do_something = "From class A"

class B:
    def do_something():
        print("From class B") # B.do_something = "From class B"

class C:
    def do_something():
        print("From class C") # C.do_something = "From class C"

print("-" * 50)





# Encapsulation

class A:
    def __init__(self, name): # Public
        self.name = name
print(A("Basel").name) # Basel

class A:
    def __init__(self, name): # Protected
        self._name = name
print(A("Basel")._name) # Basel

class A:
    def __init__(self, name): # Private
        self.__name = name
print(A("Basel").__name) # Error 

print("-" * 50)


# Getter & Setter in private only
class A:
    def __init__(self, name): # Private
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        self.__name = new_name

# Give results
one = A("Basel")
print(one.get_name()) # Give the private name
one.set_name("Sayed") # Change the private name
print(one.get_name()) # Give the new name

print("-" * 50)

# Not Give results
one.__name = "Sayed" # Not Change the private name
print(one.__name) # Error





print("-" * 50)




# Property
class A:
    def __init__(self, name): 
        self.name = name
    
    def say_hello(self):
        return f"Hello {self.name}"
    
    @property
    def say_bye(self):
        return f"Bye {self.name}"

one = A("Basel")
print(one.say_hello()) # method with () => result
print(one.say_bye()) # @property + method with () => Error
print(one.say_hello) # method without () => Informations of method
print(one.say_bye) # @property + method without () => result
    




# Abstractmethod
from abc import ABCMeta, abstractmethod

class Programming(metaclass=ABCMeta):
    @abstractmethod
    def has_oop(self):
        pass

class Python(Programming):
    def has_oop(self):
        return "Yes"

class Pascal(Programming):
    def has_oop(self):
        return "No"


one = Programming()
print(one.has_oop()) # Error 

two = Python()
print(two.has_oop()) # Yes

three = Pascal()
print(three.has_oop()) # No