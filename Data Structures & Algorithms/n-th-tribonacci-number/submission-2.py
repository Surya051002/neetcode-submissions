class Solution:
    def tribonacci(self, n: int) -> int:

        arr=[0,1,1]

        if n==0:
            return 0
        if n==1:
            return 1
        
        for i in range(3,n+1):
            # print(arr)
            arr.append(arr[i-1]+arr[i-2]+arr[i-3])
        # print(arr)
        return arr[n]
        