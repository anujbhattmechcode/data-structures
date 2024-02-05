from typing import Sequence, Optional, Any


class Queue:
    """
    This class implements Queue data structure following FIFO principle, currently only int data type
     elements are allowed
    """
    def __init__(self, data: Optional[Sequence[int] | int] = None):
        """
        :param data: (int or Sequence of int) Any int or sequence(list, tuple, etc)
        """
        self.__queue = list()
        self.__add_data(data)
        self.__count = 0

    def __add_data(self, source: int | Sequence[int]) -> None:
        if isinstance(source, Sequence):
            for i in source:
                Queue.__dtype_check(i)
                self.__queue.append(i)
        else:
            Queue.__dtype_check(source)
            self.__queue.append(source)

    @staticmethod
    def __dtype_check(entity: Any) -> None:
        if not isinstance(entity, int):
            raise TypeError("Only integer type is allowed!")

    def __len__(self):
        return len(self.__queue)

    def is_empty(self):
        return len(self.__queue) == 0

    def enqueue(self, data: int) -> None:
        """
        Inserts the element at last
        :param data: (int) integer element
        :return: None
        """
        self.__queue.append(data)

    def dequeue(self) -> int:
        """
        Removes the element first most element
        :return: (int) removed element
        """
        if not self.is_empty():
            return self.__queue.pop(0)
        else:
            raise ValueError("Empty Queue!")

    def __iter__(self):
        self.__count = 0
        return self

    def __repr__(self):
        return f"Queue({self.__queue})"

    def __next__(self):
        if self.__count < len(self.__queue):
            val = self.__queue[self.__count]
            self.__count += 1
            return val
        else:
            self.__count = 0
            raise StopIteration
