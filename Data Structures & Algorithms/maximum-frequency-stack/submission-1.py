class FreqStack:

    def __init__(self):
        self.stack=[]
        self.hashmap={}

    def push(self, val: int) -> None:
        count=self.hashmap.get(val,0)+1
        self.hashmap[val]=count
        templist=[]
        while len(self.stack)>0:
            if self.stack[-1][1]>count:
                templist.append(self.stack.pop())
            else:
                break
        self.stack.append([val,count])
        for i in range(len(templist)-1,-1,-1):
            self.stack.append(templist[i])
        # print(self.stack)
    def pop(self) -> int:
        val=self.stack.pop()[0]
        self.hashmap[val]-=1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()