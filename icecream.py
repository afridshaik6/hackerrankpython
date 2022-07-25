n = 6
arr = [1, 3, 4, 5, 6]
count = 0
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == n:
            print(i+1, j+1)
