ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
d = {}
for i in ar:
    if i not in d:
        d[i] = ar.count(i)
count = 0
for i in d:
    if ( d[i] // 2) <=0:
        pass
    else:
        c = d[i]//2
        count += c
print(count)
