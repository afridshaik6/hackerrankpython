#
# arr = [5, 4, 4, 2, 2, 8]
# result = []
#
#
#
# def all_zeros(arr):
#     for j in arr:
#         if j != 0:
#             return False
#     return True
#
#
# def getmin(arr):
#     min_value = 10**8
#     for i in arr:
#         if i<min_value and i!=0:
#             min_value = i
#     return min_value
#
#
# while not all_zeros(arr):
#     minimum = getmin(arr)
#     c = 0
#     for k in range(len(arr)):
#         if arr[k]!=0:
#             arr[k] = arr[k] - minimum
#             c += 1
#     result.append(c)
#
# print(result)
#


# def add(a,b):
#     return a+b
#
# def add2(a,b):
#     print(a+b)
#
# c = add(1,2)
# d = add2(4,5)
# print()

#
# n = 5
# c = 1
# p = 0
#
# for i in range(1, n + 1):
#     c = c * i
#
# print(c)
def fucn(n):
    if n<=1:
        return 1
    else:
        return n * fucn(n-1)
print(fucn(3))
