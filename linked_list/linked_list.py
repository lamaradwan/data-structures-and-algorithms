#Algorithm for insert:
# 1. Declare a head pointer and make it as NULL.
# 2. Create a new node with the given data.
# 3. Make the new node points to the head node.
# 4. Finally, make the new node as the head node.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def Insert(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

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
            return
        current = self.head
        while(current.next != None):
            current = current.next
        current.next = newNode


    def InsertBefore(self,data,newData):
        newNode = Node(newData)
        if self.head == None:
            self.head = newNode
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
                return
            current = current.next
        if current.data != data:
            raise Exception(f"The Index {data} is not exist in the list")


    def InsertAfter(self,data,newData):
        newNode = Node(newData)
        if self.head == None:
            self.head = newNode
            return
        current = self.head
        while current.next != None:
            nextNode = current.next
            if current.data == data:
                current.next = newNode
                newNode.next = nextNode
                return
            current = current.next
        if current.data == data:
            self.Append(newData)
            return
        if current.data != data:
            raise Exception(f"The Index {data} is not exist in the list")


if __name__ == '__main__':
    list = LinkedList()
    list.Insert(10)
    list.Insert(20)
    list.Insert(30)
    list.Append(2)
    list.Insert(40)
    list.Append(5)

    list.InsertAfter(30,8)
    list.InsertAfter(2,200)
    # list.InsertAfter(100,500)

    list.InsertBefore(40,9)
    list.InsertBefore(10,9)
    # list.InsertBefore(400,9)


    # list.Append(2)


    str(list.ToString())
    # print(list.head.data)
    # print()
    # print(list.Includes(10))


