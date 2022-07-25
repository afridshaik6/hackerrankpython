parrot="Norwegian Blue"
print(parrot[0:14:3]) #Nen
print(parrot[-8])#i
print(parrot[11:-13:-4])
print(parrot[::-1])#
print(parrot[::-3])#eBaeo

number= "9,223;372:036 854,775;807"
seperators= number[1::4]
print(seperators)
values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])