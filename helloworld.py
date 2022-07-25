array = []
array = [int(item) for item in input("Enter the list items : ").split()]
print(array)


def miniMaxSum(arr):
    # Write your code here
    new_min_array = [i for i in arr if i != max(arr)]
    sum_min = sum(new_min_array)
    new_max_array = [i for i in arr if i != min(arr)]
    sum_max = sum(new_max_array)
    print(sum_min, sum_max)


miniMaxSum(array)