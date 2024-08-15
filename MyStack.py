# 225. Implement a Stack using Queues

'''
Implement a Stack class using only queues
'''

from collections import deque

class MyStack:
    
    def __init__(self):
        self.queue = deque()
    
    def push(self, x: int) -> None:
        print(f"push: {x}")
        self.queue.appendleft(x)
        self.print_stack()
        pass
    
    def pop(self) -> int:
        if not self.empty():
            popped = self.queue.popleft()
            print(f"popped: {popped}")
            return popped
        pass

    def top(self) -> int:
        if not self.empty():
            top = self.queue[0]
            print(f"top: {top}")
            return top
        pass
    
    def empty(self) -> bool:
        print(len(self.queue))
        return len(self.queue) == 0
    
    def print_stack(self):
        print(f"stack: {self.queue}")

def main():
    stack = MyStack()
    stack.empty()
    stack.push(1)
    stack.push(2)
    stack.top() # return 2
    stack.pop() # return 2
    stack.empty() # False
    
if __name__ == '__main__':
    main()