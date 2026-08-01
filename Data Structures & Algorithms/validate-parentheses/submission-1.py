class Solution:
    def isValid(self, s: str) -> bool:
        opens=["(","{","["]
        # closes=[")","}","]"]
        stack=[]
        for i in s:
            if(i in opens):
                stack.append(i)
            else:
                if(len(stack)==0):
                    return False
                val=stack.pop()
                if("("==val and i==")"):
                    continue
                elif "{" == val and i== "}":
                    continue
                elif "[" ==val and i=="]" :
                    continue
                else:
                    return False
        if(len(stack)>0):
            return False
        return True




        