# __init__ => انشاء نموذج اساسي لاي شيء يؤخذ منه لعمل العديد من النسخ => def__init__(self):
# __class__ => معرفة اي كلاس ينتمي اليه المتغير ده => print(variable.__class__)
# __str__ => عندما تطبع الكلاس زي ما هو من غير اما تنادي اي حاجه جواه يعطك كلام غير مفهوم اما عندما تستعمل هذه يطبعلك ما تحتها من غير مناداتها => def__str__(self):
# __len__ => عندما تسأل عن طول عناصر ال __init__ بدونه باستخدام len(class_name) لا يعطيك شيء ولكن عند استعماله يعطك طول اللي جوا __init__ => def__len__(self):




# __class__

class User:
    def __init__(self):
        self.name = "Basel"
    
user_name = User()
print(user_name.__class__)
print(type(user_name))

print("-" * 50)








# __str__

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


class User:
    def __init__(self):
        self.name = "Basel"
    def hello(self):
        return(f"My name is {self.name}")
    
user_name = User()
print(user_name)
print(user_name.hello())









# __int__

class User:
    def __init__(self):
        self.name = "Basel"
    
user_name = User()





class User:
    def __init__(self):
        self.name = "Basel"
    def __len__(self):
        return len(self.name)
    
user_name = User()
print(len(user_name))