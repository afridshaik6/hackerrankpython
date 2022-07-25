n = 3
password = "#HackerRank"
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"


l = [0, 0, 0, 0]
if len(password) >=6:
    for i in password:
        if i.isdigit():
            l[0] = 1
        elif i.islower():
            l[1] = 1
        elif i.isupper():
            l[2] = 1
        elif i in special_characters:
            l[3] = 1
    print(4 - sum(l))

