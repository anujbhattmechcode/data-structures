from data_structures import SinglyLinkedList


ll = SinglyLinkedList([1, 2, 3, 4, 5])
print(ll)

ll.add(12)
print(ll)

for i in ll:
    print("Element: ", i)

print("Length of the linked list: ", ll.length)
print(ll)
