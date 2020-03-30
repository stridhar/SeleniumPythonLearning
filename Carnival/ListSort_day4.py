std=["arvind","kumar","vijaya","lakshmi"]
print("Before sort ",std)
std.sort()
print("After sort ",std)

#zipping
std=["arvind","kumar","vijaya","lakshmi"]
cor=["python","java","scala","android"]
for x in zip(std,cor):
    print(x)
print("Total no of std: ",len(std))
print(std[::-1])

name = "arvind"
print(name[::1])
print(name[:-3:-1])
