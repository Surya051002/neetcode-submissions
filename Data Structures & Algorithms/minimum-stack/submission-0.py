class MinStack:

    def __init__(self):
        self.stack=[]
        self.minval=[float("inf")]
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minval.append(min(self.minval[-1],val))

    def pop(self) -> None:
        self.stack.pop()
        self.minval.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.minval[len(self.minval)-1]

        

        
