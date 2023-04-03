class myclassloluwupogges:
    x = 5

p1 = myclassloluwupogges()

print(p1.x)


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}({self.age})"
    
    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = person("John", 36)

print(p1.name)
print(p1.age)
print(p1)

p1.myfunc()