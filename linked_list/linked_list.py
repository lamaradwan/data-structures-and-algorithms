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




if __name__ == '__main__':
    list = LinkedList()
    list.Insert(10)
    list.Insert(20)
    list.Insert(30)
    list.Insert(40)


    str(list.ToString())
    print(list.head.data)
    # print()
    # print(list.Includes(10))


