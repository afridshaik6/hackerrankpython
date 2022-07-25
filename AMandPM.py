def fucn():
    s = input("time is : ")
    if "PM" in s and s[:2] == "12":
        return s
    elif "PM" in s and s[:2] != "12":
        return str(int(s[:2]) + 12) + s[2:]
    if "AM" in s and s[:2] == "12":
        return "00" + s[2:]
    elif "AM" in s and s[:2] != "12":
        return s


print(fucn())