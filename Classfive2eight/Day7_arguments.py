class Methods():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("I am a constructor")
    def param1(self,a):
        print("Single param", a)
    def paramMulti(self,*args):
        print("Multiple param", args)
    def paramMultiKeyValue(self,**kwargs):
        print("Multiple keyvalue param",kwargs)

m=Methods("Sridhar",42)
m.param1("Vijaya")
m.paramMulti("Vijaya","Sridhar","Raj","Mitali","Arpita")
m.paramMultiKeyValue(name="aravind",age=36,hobby="reading")