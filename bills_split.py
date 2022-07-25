bill = [3, 10, 2, 9]
k = 1
new_bill = []
for i in range(len(bill)):
    if i == k:
        pass
    else:
        new_bill.append(bill[i])
print(new_bill)
