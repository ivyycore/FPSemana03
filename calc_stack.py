from collections import deque
numbers = input()
stack = deque()
stack_2 = deque()

for number in numbers.split (" "):
    stack.append(int(number))
print(stack)

while len(stack)>0:
    n=stack.pop() * 2
    print(n)
    