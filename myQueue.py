# Queue implementation using stacks
# methods: push(int), int pop(), int peek(), bool empty()


# approach:
# very easy First in First Out (FIFO) method
# self.size is actually not really necessary so it depends on programming language
class myQueue:
    def __init__(self):
        print('init')
        self.queue = []
        # self.size = 0
    # push
    def push(self, x: int) -> None:
        self.queue.append(x)
        # self.size += 1
    # pop
    def pop(self) -> int:
        return(self.queue.pop(0))
        # self.size -= 1
    # peek
    def peek(self) -> int:
        return self.queue[0]
    # empty
    def empty(self) -> bool:
        return False if self.queue else False
        # return True if self.size == 0 else False

def main():
    q = myQueue()
    q.push(1); print(q.queue)
    q.push(2); print(q.queue)
    print(q.peek()); print(q.queue)
    print(q.pop()); print(q.queue)
    print(q.empty()); print(q.queue)


if __name__ == '__main__':
    main()
