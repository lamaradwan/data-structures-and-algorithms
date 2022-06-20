from linked_list.linked_list import LinkedList
def zipLists(list1, list2):
    # Start pointing the nodes
    curr1 = list1.head
    curr2 = list2.head
    while curr1 != None and curr2 != None:
        next1 = curr1.next
        next2 = curr2.next
        curr2.next = next1
        curr1.next = curr2
        curr1 = next1
        curr2 = next2
        list2.head = curr2
    #Handle the case where list1 become empty before list2
    if curr2:
        list1.Append(curr2.data)
    return list1.ToString()


if __name__ == '__main__':
    list1 = LinkedList()
    list1.Append(1)
    list1.Append(3)
    list1.Append(2)

    list2 = LinkedList()
    list2.Append(5)
    # list2.Append(9)
    # list2.Append(4)

    list1.ToString()
    print()
    list2.ToString()
    print()

    zipLists(list1,list2)