class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        n=len(heights)
        max_area=0
        for index,height in enumerate(heights):
            i=index
            while(len(stack)>0 and stack[-1][0]>height):
                val=stack.pop()
                max_area=max(max_area,(index-val[1])*val[0])
                i=val[1]
            stack.append([height,i])
        
        while len(stack)>0:
            val=stack.pop()
            max_area=max(max_area,(n-val[1])*val[0])
        return max_area

        


        