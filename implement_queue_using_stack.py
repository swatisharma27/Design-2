from collections import deque
class MyQueue:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        
    def push(self, x: int) -> None:
        self.q1.append(x)

    def rotate(self):
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self. q1

    def pop(self) -> int:
        self.rotate()
        if self.q1:
            return self.q1.popleft()
        
    def peek(self) -> int:
        self.rotate()
        if self.q1:
            return self.q1[0]
        else:
            return None


    def empty(self) -> bool:
        return not self.q1 and not self.q2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()