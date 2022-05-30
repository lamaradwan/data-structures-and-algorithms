
def reverseArray(array):
    if len(array) == 0:
        return "Empty Array"
    else:
        return array[::-1]

employees = [
    {
        "Name":"Lama Radwan",
        "Department": "Development",
        "Age": 23
    },
    {
        "Name": "Rawan Ahmad",
        "Department": "Accounting",
        "Age": 27
    },
    {
        "Name": "Hiba Shahid",
        "Department": "Management",
        "Age": 30
    }
]

#Test Cases
print(reverseArray([0,2,4,6,8,10]))
print(reverseArray([-1,-7,-5,-10,-90]))
print(reverseArray([1,1,5,1,1]))
print(reverseArray([3,3,3,3,3]))
print(reverseArray([0]))
print(reverseArray([2.04,5.60,10.45,1.98,8.89]))
print(reverseArray(["Hi","Lama","Testing"]))
print(reverseArray(employees))
