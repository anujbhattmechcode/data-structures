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
