class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        c=""
        i=0
        n=len(s)

        while i<n:
            if(s[i]==']'):
                if(c!=""):
                    stack.append(c)
                tempans=""
                while stack[-1]!='[':
                    t=stack.pop()
                    # print(t,tempans)
                    t+=tempans
                    tempans=t
                stack.pop()
                val=stack.pop()
                stack.append(val*tempans)
                c=""

            elif s[i]=='[':
                if c!="":
                    stack.append(c)
                stack.append('[')
                c=""
                # print(stack)
            elif ord(s[i])<97:
                if(c!=""):
                    stack.append(c)
                    c=""
                while ord(s[i])<=ord('9') and ord(s[i])>=ord('0'):
                    c+=s[i]
                    i+=1
                stack.append(int(c))
                c=""
                continue
            else:
                c+=s[i]
            i+=1
        if(c!=""):
            stack.append(c)
        
        # print(stack)
        return "".join(stack)
                


        