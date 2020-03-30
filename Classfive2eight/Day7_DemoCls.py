class Methods():
    #Global variable
    global state
    state="Karnataka"
    city = "Bangalore"
    def __init__(self):
        print("I am a constructor")
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("I am a constructor")
    def normalMethod(self):
        print("I am a normal method")
        print(state)
        print(self.city)
    def expVariable(self):
        print("My name is ",self.name)
        print("My age is ",self.age)
#Object of the class
m=Methods("Sridhar",42)
m.normalMethod()
m.expVariable()