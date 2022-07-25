# y = []
# k = [i+1 for i in range(len(p))]
#
# x = 0
# for x in range(len(p)):
#
#     for i in range(len(p)):
#         if p[i] == k[x]:
#             c = i + 1
#             for j in p:
#                 if j == c:
#                     last_num = p.index(j) + 1
#                     y.append(last_num)
#
#
# # print(y)
# p = [i for i in range(1000)]
p = [2,2,3,4,5]
s=set(p)
h = []
count = 0
d = 1
for i in range(len(p)):
    for j in range(i+1,len(p)):
        if p[j] - p[i] == d and p[j]+d in s:
            count+=1
print(count)



