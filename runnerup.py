n = int(input("enter the number : "))
arr = [6,6,6,6]
new_arr = set(arr)
new_arr.remove(max(arr))
print(max(new_arr))

