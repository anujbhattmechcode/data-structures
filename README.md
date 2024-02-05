## Data Structures ##
Various data structures such as linked list, stacks and queues implementation in python

### Examples ###
1. Linked List

    refer linked_list_example.py 

```python
from data_structures import SinglyLinkedList


ll = SinglyLinkedList([1, 2, 3, 4, 5])
print(ll)

ll.add(12)
print(ll)

for i in ll:
    print("Element: ", i)

print("Length of the linked list: ", ll.length)
print(ll)
```
*OUTPUT:*
```bash
Node: DATA 1 NEXT 2
LinkedList:
	Length: 5
	Head: Node: DATA 1 NEXT 2
LinkedList:
	Length: 6
	Head: Node: DATA 1 NEXT 2
Element:  Node: DATA 1 NEXT 2
Element:  Node: DATA 2 NEXT 3
Element:  Node: DATA 3 NEXT 4
Element:  Node: DATA 4 NEXT 5
Element:  Node: DATA 5 NEXT 12
Element:  Node: DATA 12 NEXT None
Length of the linked list:  6
LinkedList:
	Length: 6
	Head: Node: DATA 1 NEXT 2
```

2. Stacks
    refer to stack_use_example.py
```python
from data_structures import Stack

stack = Stack([1, 2, 3, 4])

stack.add(4)
print(stack)

v1 = stack.pop()
v2 = stack.pop()
print(v1, v2, stack, sep="\n")
print(f"Length of the stack: {len(stack)}")

# Follows LIFO
for i in stack:
    print("Elements: ", i)
```
*OUTPUT:*
```bash
Stack([1, 2, 3, 4, 4])
4
4
Stack([1, 2, 3])
Length of the stack: 3
Elements:  3
Elements:  2
Elements:  1
```

3. Stacks
    refer to queue_use_example.py
```python
from data_structures import Queue

queue = Queue([1, 2, 3, 4])
print(queue)

queue.enqueue(4)

v1 = queue.dequeue()
v2 = queue.dequeue()
print(v1, v2, queue, sep="\n")
print(f"Length of the queue: {len(queue)}")

# Follows FIFO
for i in queue:
    print("Elements: ", i)

```
*OUTPUT:*
```bash
Queue([1, 2, 3, 4])
1
2
Queue([3, 4, 4])
Length of the queue: 3
Elements:  3
Elements:  4
Elements:  4
```
