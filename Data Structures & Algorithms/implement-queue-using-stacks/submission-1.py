class MyQueue:

    def __init__(self):
        self.stack=[]

    def push(self, x: int) -> None:
        newstack=[]
        newstack.append(x)
        while  len(self.stack)>0:
            t=self.stack.pop(0)
            newstack.append(t)
        
        self.stack=newstack

    def pop(self) -> int:
        return self.stack.pop()


    def peek(self) -> int:
        return self.stack[len(self.stack)-1]

    def empty(self) -> bool:
        return True if len(self.stack)<=0 else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()