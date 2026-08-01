from queue import Queue
class MyStack:

    def __init__(self):
        self.q=Queue()

    def push(self, x: int) -> None:
        que=Queue()
        que.put(x)
        while not self.q.empty():
            que.put(self.q.get())
        self.q=que

    def pop(self) -> int:
        return self.q.get()
        

    def top(self) -> int:
        return self.q.queue[0]
    def empty(self) -> bool:
        return self.q.empty()
        
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()