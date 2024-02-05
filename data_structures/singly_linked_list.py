from typing import List


class Node:
    """
    Node class to create nodes for the Linked List, it can have int data type as element for now
    """
    def __init__(self, data: int):
        self.data = data
        self.next = None

    def __repr__(self):
        next_ref = self.next.data if self.next else None
        return f"Node: DATA {self.data} NEXT {next_ref}"


class SinglyLinkedList:
    """
    Singly linked list having only head, it implements Linked List data structure using Nodes class for nodes
    """
    def __init__(self, source: List[int] | int):
        """
        :param source: (int or Sequence of int) Any int or sequence(list, tuple, etc)
        """
        self.head = None
        self.__count = 0
        self.__source_init(source)
        print(self.head)
        self.__c = self.head

    def __cnt_increment(self):
        self.__count += 1

    def add(self, data: int):
        """
        Adds the given data into the element
        :param data: (int) int element
        :return: None
        """
        node = Node(data)
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = node
        else:
            self.head = node

        self.__cnt_increment()

    def __source_init(self, source: List[int] | int):
        if isinstance(source, int):
            self.add(source)
        elif isinstance(source, list):
            for i in source:
                self.add(i)

    def __repr__(self):
        return f"LinkedList:\n\tLength: {self.__count}\n\tHead: {self.head}"

    def traverse(self):
        """
        Traverses through the linked list and prints the data values
        :return: None
        """
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    @property
    def length(self):
        return self.__count

    def __iter__(self):
        self.__c = self.head
        return self

    def __next__(self):
        if self.__c and self.__c.data:
            val = self.__c
            self.__c = self.__c.next
            return val
        else:
            self.__c = self.head
            raise StopIteration
