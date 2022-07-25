d={}
for _ in range(int(input())):
    name = input()
    score = float(input())
    if score not in d:
        d[score]= [name]
    else:
        d[score].append(name)
min_key = min(d.keys())
del d[min_key]
new_minimum = min(d.keys())
sorted_names = sorted(d[new_minimum])
for i in sorted_names:
    print(i)
