import math

def insertShiftArray(array,input):
    if len(array) == 0:
        return "Empty List"
    elif input == " ":
        return "Element is empty"
    else:
        length = len(array)
        half = math.ceil(len(array)/2)
        array[half:] = [input] + array[half:length]
        return array

employees = [
    {
        "Name":"Lama Radwan",
        "Department": "Development",
        "Age": 23
    },
    {
        "Name": "Hiba Shahid",
        "Department": "Management",
        "Age": 30
    }
]

#Testcases
print(insertShiftArray([1,2,3,3,2,1],0))
print(insertShiftArray([2],5))
print(insertShiftArray([-1,-7,-5,-10,-90],-3))
print(insertShiftArray([-1,-7,-5,-10,-90]," "))
print(insertShiftArray([],4))
print(insertShiftArray([2.04,5.60,10.45,1.98,8.89],99))
print(insertShiftArray(["Hi","Lama","Testing"],"is not"))
print(insertShiftArray(employees,6))
print(insertShiftArray(employees,    {
        "Name": "Rawan Ahmad",
        "Department": "Accounting",
        "Age": 27
    }))



"""Stretch Goal
Write a second function that removes an element from
the middle index and shifts other elements in the array to fill the new gap."""
def removeShiftArray(array):
    length = len(array)
    half = math.floor(len(array) / 2)
    array[half:] = array[half+1:length]
    return array

print(removeShiftArray([1,2,5,3,2]))