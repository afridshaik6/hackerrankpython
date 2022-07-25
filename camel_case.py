s = "oneTwoThree"
empty_list = []
for i in range(len(s)):
    if s[i].isupper():
        empty_list.append(s[:i])


print(empty_list)

