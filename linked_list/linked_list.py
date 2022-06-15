#Algorithm for insert:
# 1. Declare a head pointer and make it as NULL.
# 2. Create a new node with the given data.
# 3. Make the new node points to the head node.
# 4. Finally, make the new node as the head node.
import math


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def Insert(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.count +=1

    def Includes(self,x):
        try:
            Temp = self.head
            if(Temp.data != x):
                while(Temp.data != x):
                    Temp = Temp.next
                return True
            else:
                return True
        except:
            return False

    def ToString(self):
        Temp = self.head
        if (Temp != None):
            list = []
            while (Temp != None):
                print("{",Temp.data,end = " } -> ")
                list.append(Temp.data)
                Temp = Temp.next
            print(end="NULL")
            return list
        else:
            print("The list is empty.")
            return "The list is empty."

    def Append(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.count+=1
            return
        current = self.head
        while(current.next != None):
            current = current.next
        current.next = newNode
        self.count+=1


    def InsertBefore(self,data,newData):
        newNode = Node(newData)
        if self.head == None:
            self.head = newNode
            self.count+=1
            return
        current = self.head
        if current.data == data:
            self.Insert(newData)
            return
        while current.next != None:
            nextNode = current.next
            if current.next.data == data:
                current.next = newNode
                newNode.next = nextNode
                self.count += 1
                return
            current = current.next

        if current.data != data:
            raise Exception(f"The Index {data} is not exist in the list")


    def InsertAfter(self,data,newData):
        newNode = Node(newData)
        if self.head == None:
            self.head = newNode
            self.count+=1
            return
        current = self.head
        while current.next != None:
            nextNode = current.next
            if current.data == data:
                current.next = newNode
                newNode.next = nextNode
                self.count+=1
                return
            current = current.next
        if current.data == data:
            self.Append(newData)
            return
        if current.data != data:
            raise Exception(f"The Index {data} is not exist in the list")


    def kthFromEnd(self,index):
        if index > self.count - 1:
            raise Exception(f"Index {index} is out of range")
        elif index < 0:
            return "Index should be a positive number"
        current = self.head
        innerCount = self.count-1
        # print(innerCount)
        while current.next != None:
            if index == innerCount:
                return current.data
            else:
                current = current.next
                innerCount -=1
                # print(innerCount)
        return current.data


if __name__ == '__main__':
    # list = LinkedList()
    # list.Insert(10)
    # list.Insert(20)
    # list.Insert(30)
    # # # list.Append(2)
    # list.Insert(40)
    # # print(list.kthFromEnd(3))
    #
    # list.Append(5)
    # list.Append(6)
    # list.Append(7)
    # list.Append(8)
    # list.InsertBefore(10, 9)
    # list.InsertBefore(9, 99)
    # list.InsertAfter(99,100)
    # print(list.kthFromEnd(10))
    # print(list.kthFromEnd(-3))
    #
    #
    # # list.InsertAfter(30,8)
    # # list.InsertAfter(2,200)
    # # list.InsertAfter(100,500)
    #
    # # list.InsertBefore(40,9)
    #
    # # list.InsertBefore(400,9)
    #
    #
    # # list.Append(2)
    #
    #
    # str(list.ToString())
    # # print(list.head.data)
    # # print()
    # # print(list.Includes(10))


    testing = LinkedList()
    testing.Append(10)
    testing.Append(15)
    # testing.Append(20)
    testing.Append(25)
    testing.Append(30)
    print(testing.kthFromEnd(1))
    print(math.floor(testing.count/2))

