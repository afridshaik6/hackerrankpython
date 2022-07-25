s1 = "acxz"
s2 = s1[::-1]
c= 0
if len(s1)%2 == 0:
for i in range(len(s2) - 1):
    if ord(s2[i]) - ord(s2[i+1]) == 1:
        c+=1
if c == len(s2) - 1:
    print("Funny")
else:
    print("Not Funny")
