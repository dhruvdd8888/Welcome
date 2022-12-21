class MyQueue:
    # l=[]
    def __init__(self):
        self.l=[]
        # print(self.l)
        

    def push(self, x: int) -> None:
        self.l.insert(0,x)

    def pop(self) -> int:
        if(self.empty()):return
        an=self.l[0]
        self.l=self.l[1:]
        return an 

    def peek(self) -> int:
        if(self.empty()):return None
        an=self.l[0]
        return an

    def empty(self) -> bool:
        if(len(self.l)==0):return True 
        return False


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()