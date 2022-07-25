arr1 = ["adbfg", "abcd", "defba", "hgadb"]
finalresult=set(arr1[0])
for i in arr1:
    finalresult=set(i).intersection(finalresult)
print(len(finalresult))