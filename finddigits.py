n=1240
count = 0
s= str(n)
for i in s:
    if i == "0":
        pass
    elif n%int(i) == 0:
        count+=1
print(count)