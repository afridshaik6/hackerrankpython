# a=[3,2,1,2,3]
# empty_list = []
#
#
# def min_dist(a):
#     for i in range(len(a)):
#         for j in range(i + 1, len(a)):
#             if a[i] == a[j]:
#                 empty_list.append(abs(i - j))
#     return min(empty_list)
a=[3,0,2]


def min_dist(a):
    d={}
    minimum_dist = 10**5
    for i in range(len(a)):
        if a[i] not in d:
            d[a[i]] = [i]
        else:
            d[a[i]].append(i)
    for i in d:
        if len(d[i])>1:
            minimum_dist=min(minimum_dist,(d[i][-1] - d[i][0]))
    if minimum_dist == 10**5:
        return -1
    else:
        return minimum_dist
print(min_dist(a))

