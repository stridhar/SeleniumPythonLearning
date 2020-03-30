word = "1abc2abc3abc4abc"
print(word.split("2"))
print(word.split("2")[0])
print(word.split("2")[1])
print(word.split("2")[1].replace("abc","ABC",1))
#now retain the old with new result
val=word.split("2")
print(val[0]+"2"+val[1].replace("abc","ABC",1))