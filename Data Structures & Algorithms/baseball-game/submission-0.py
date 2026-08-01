class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        length=-1
        for operation in operations:
            print(length)
            if (operation=="+"):
                temp1=stack[length]
                temp2=stack[length-1]
                stack.append(temp1+temp2)
                length+=1
            elif operation=="D":
                stack.append(stack[length]*2)
                length+=1
            elif operation=="C":
                stack.pop(length)
                length-=1
            else:
                if(length+1==len(stack)):
                    stack.append(int(operation))
                    length+=1
                else:
                    length+=1
                    stack[length]=int(operation)
        sum=0
        for j in stack:
            sum+=j
        return sum

        