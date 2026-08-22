class MyCircularQueue:

    def __init__(self, k: int):
        self.arr=[-1]*(k+1)
        self.front=-1
        self.rear=0

    def enQueue(self, value: int) -> bool:
        
        if self.isFull():
            return False
        self.arr[self.rear]=value
        self.rear=(self.rear+1)%len(self.arr)
        if self.front==-1:
            self.front+=1
        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front=(self.front+1)%len(self.arr)
        return True
    def Front(self) -> int:
        if self.front==self.rear:
            return -1
        return self.arr[self.front]

    def Rear(self) -> int:
        if self.rear==self.front:
            return -1
        if self.rear==0:
            return self.arr[len(self.arr)-1]
        return self.arr[self.rear-1]

    def isEmpty(self) -> bool:
        if self.front ==-1 or self.front==self.rear:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if (self.rear+1)%len(self.arr) ==self.front:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()