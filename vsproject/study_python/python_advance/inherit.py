#class Parent(object):
#    def __init__(self, name, *args, **kwargs):
#        print("Parent init begin")
#        self.name = name
#        print("Parent init end")

#class Son1(Parent):
#    def __init__(self, name, age, *args, **kwargs):
#        print("Son1 init begin")
#        self.age = name
#        super().__init__(name, *args, **kwargs)
#        print("Son1 init end")

#class Son2(Parent):
#    def __init__(self, name, gender, *args, **kwargs):
#        print("Son2 init begin")
#        self.gender = gender
#        super().__init__(name, *args, **kwargs)
#        print("Son2 init end")

#class Grandson(Son1, Son2):
#    def __init__(self, name, age, gender):
#        print("Grandson init begin")
#        self.gender = gender
#        super().__init__(name, age, gender)
#        print("Grandson init end")

#print(Grandson.__mro__)
#g = Grandson("yd", 18, "man")

#t = (1, 2, 3, 4)
#print(*t)

#d = {"yd":18, "yy":18}
#print(**d)

class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)