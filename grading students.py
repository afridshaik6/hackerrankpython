# # # # def func(n):
# # # #     l=[]
# # # #     for i in range(n):
# # # #         l.append(i)
# # # #     return l
# # # # print(func(5))
# # # #
# # # #
# # # # def fun():
# # # #     return 1
# # # # #
# # # # def fun1():
# # # #     print(1)
# # # #
# # # # a = fun()
# # # # b = fun1()
# # # # print()
# # # def gradingStudents(grades):
# # #     p=[]
# # #     for i in grades:
# # #         if i<38:
# # #             p.append(i)
# # #         if i%5<3:
# # #             p.append(i)
# # #         else:
# # #             k= i+(5-(i%5))
# # #             p.append(k)
# # #     return p
# # #
# # #
# # # print(gradingStudents([]))
# # #
# # List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# #
# # # Show original list
# # print("\nOriginal List:\n", List)
# #
# # print("\nSliced Lists: ")
# #
# # # Display sliced list
# # print(List[3:9:2])
# #
# # # Display sliced list
# # print(List[::2])
# #
# # # Display sliced list
# # print(List[::])
# # l="heloo world"
# # print(l[1:8])
# charc_heights = {}
# p = list(map(chr, range(97, 123)))
# h = [19, 13, 22, 6, 25, 1, 15, 11, 20, 18, 4, 16, 9, 21, 24, 12, 17, 7, 3, 2, 10, 14, 26, 23, 8, 0]
# for i in range(len(p)):
#     charc_heights[p[i]]= h[i]
# print(charc_heights)
# word="hello"
# num_list=[]
# for i in word:
#     if i in charc_heights:
#         num_list.append(charc_heights[i])
# print(num_list)
# print(max(num_list) * len(word))
k = 23047885
list_1 = []
for i in range(1, 2000001):
    list_1.append(i)
# print(list_1)
list_2 = []
for i in list_1:
    list_2.append(str(i))
# print(list_2)
list_3 = []
for i in range(4):
    c = list_2[i][::-1]
    list_3.append(c)
# print(list_3)
list_4 = []
for i in list_3:
    list_4.append(int(i))
# print(list_4)
sub = []
for i in range(len(list_1)):
    sub.append(abs(list_1[i] - list_4[i]))
print(sub)
count = 0
for i in sub:
    if i % k == 0:
        count += 1
print(count)

#
