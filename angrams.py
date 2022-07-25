def makingAnagrams(s1, s2):
    # Write your code here
    newlist = []
    for i in s1:
        if i in s2:
            newlist.append(i)
    new_s1 = list(s1.strip(" "))
    new_s2 = list(s2.strip(" "))
    print(new_s2)
    for i in new_s1:
        if i in newlist:
            s1.remove(i)
    for i in new_s2:
        if i in newlist:
            s2.remove(i)
    return (len(s1) + len(s2))

print(makingAnagrams("cde" , "abc"))
