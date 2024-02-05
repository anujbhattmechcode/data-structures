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
