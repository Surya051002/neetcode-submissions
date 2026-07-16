class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        n=len(nums)
        for i in nums:
            d[i]=d.get(i,0)+1
        ans=[]
        for item in d.items():
            if item[1]> n//3:
                ans.append(item[0])

        return ans
        