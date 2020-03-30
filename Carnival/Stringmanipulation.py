#upper, lower
name="Sarvesh"
print("Upper case: ",name.upper())
print("Lower case: ", name.lower())

#Split
name="Sarves_34567890"
fn=name.split("_")[0]
ac=name.split("_")[1]
print("Split 1: ", fn)
print("Split 2: ", ac)

name="Sarves_34567890#Hydrabad"
fn=name.split("_")[0]
ac=name.split("_")[1]
city=ac.split("#")[1]
print(fn),print(ac),print(city)