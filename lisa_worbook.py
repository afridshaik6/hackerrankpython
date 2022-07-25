k = 3
arr = [4, 2, 6, 1, 10]
result_list = []

for i in arr:
    result_list.append([])
    count = 0
    for j in range(1, i + 1):
        if count < 3:
            result_list[-1].append(j)
            count += 1
        else:
            result_list.append([])
            result_list[-1].append(j)
            count = 1

final_count = 0
number = 1
for i in result_list:
    if number in i:
        final_count += 1
    number += 1
print(result_list)
print(final_count)
