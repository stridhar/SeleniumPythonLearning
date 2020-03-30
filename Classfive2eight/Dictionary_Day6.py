#Dictionary
cars = {"color":"red","doors":"4"}
print(type(cars))
#To print the dictionary, keys and values
print(cars)
print(cars.keys())
print(cars.values())
#To loop the entire dictionary
for l in cars.items():
    print(l)

cars["wheels"]="4"
print(cars)

cars.pop("wheels")   #In dict pop we have to give one argument
print(cars)

cars.clear()
print(cars)
