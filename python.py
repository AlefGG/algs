from collections import deque
from linked_list import LinkedList
from min_stack import MinStack
from min_queue import MinQueue


class MyStack:
    
    def __init__(self):
        self.q = deque()
        self.temp = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
    
    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            val = self.q.popleft()
            self.temp.append(val)
        ans = self.q.popleft()
        self.q = deque(self.temp) 
        self.temp.clear()
        return ans

    def top(self) -> int:
        self.temp = deque(self.q)
        for i in range(len(self.q) - 1):
            self.temp.popleft()
        ans = self.temp.popleft()
        self.temp = deque()
        return ans
    
    def empty(self) -> bool:
        return len(self.q) == 0


    

    def toString(self):
        print(self.q)

stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.toString()
stack.pop()
stack.toString()
print(stack.top())
stack.toString()
print(stack.empty())
stack.pop()
stack.pop()
stack.toString()
print(stack.empty())