# fo=open("name.txt","r")
# # fo.write( "Python is a great language.\nYeah its great!!\n")
# # fo.close()
# print(fo.read(10))
# print(fo.read())
class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
print(emp1)
