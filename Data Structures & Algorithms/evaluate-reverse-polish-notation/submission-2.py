class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:

            if(token=="+"):
                t1=stack.pop()
                t2=stack.pop()
                stack.append(t1+t2)
            elif token=="-":
                t1=stack.pop()
                t2=stack.pop()
                stack.append(t2-t1)
            elif token=="*":
                t1=stack.pop()
                t2=stack.pop()
                stack.append(t1*t2)
            elif token=="/":
                t1=stack.pop()
                t2=stack.pop()
                stack.append(int(t2/t1))
            else:
                stack.append(int(token))
        return stack.pop()

        