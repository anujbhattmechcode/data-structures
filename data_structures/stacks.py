"""
Stack Data Structure implementation using python lists.
Currently only int data type elements are supported in stacks
"""
from typing import Sequence, Any, Optional


class Stack:
    """
    This class provides Stack Data Structure like ADT, following the LIFO (Last In First Out) protocol
    """
    def __init__(self, source: int | Sequence[int]) -> None:
        """
        :param source: (int or Sequence of int) Any int or sequence(list, tuple, etc)
        of int to initialize the stack
        """
        self.__stack = []
        self.__add_data(source)
        self.__count = len(self.__stack) - 1

    def __is_empty(self):
        return self.__count == 0

    def __len__(self):
        return self.__count

    def __add_data(self, source: int | Sequence[int]) -> None:
        if isinstance(source, Sequence):
            for i in source:
                Stack.__dtype_check(i)
                self.__stack.append(i)
        else:
            Stack.__dtype_check(source)
            self.__stack.append(source)

    @staticmethod
    def __dtype_check(entity: Any) -> None:
        if not isinstance(entity, int):
            raise TypeError("Only integer type is allowed!")

    def add(self, source: int) -> None:
        """
        Adds the element in the stack as LIFO principle
        :param source: (int) int element
        :return: None
        """
        Stack.__dtype_check(source)
        self.__stack.append(source)

    def pop(self) -> Optional[int]:
        """
        Removes the element from the stack as LIFO principle
        :return: (int) Latest inserted element
        """
        if len(self.__stack) == 0:
            return None
        return self.__stack.pop()

    def __repr__(self):
        return f"Stack({self.__stack})"

    def __iter__(self):
        self.__count = len(self.__stack) - 1
        return self

    def __next__(self):
        if self.__count >= 0:
            val = self.__stack[self.__count]
            self.__count -= 1
            return val
        else:
            self.__count = len(self.__stack) - 1
            raise StopIteration
