from collections import deque
nomes = input()
stack = deque()
stack_2 = deque()

for nome in nomes.split (" "):
    stack.appendleft(str(nome))
print(stack)

while len(stack) >0:
    l = stack.pop()
    if 'a' in l:
        print(l)