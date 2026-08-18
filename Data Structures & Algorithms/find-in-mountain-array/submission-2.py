class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        left=0
        right=mountainArr.length()-1
        midpos=0
        while left<=right:

            mid=left+(right-left)//2

            l=mountainArr.get(mid-1)
            m=mountainArr.get(mid)
            r=mountainArr.get(mid+1)

            if l<m and m>r:
                midpos=mid
                break
            elif l<m and m<r:
                left=mid+1
            else:
                right=mid-1
        left=0
        right=midpos
        print(midpos)
        while left<=right:

            mid=left+(right-left)//2
            midval=mountainArr.get(mid)
            if midval==target:
                return mid
            elif midval<target:
                left=mid+1
            else:
                right=mid-1
        left=midpos+1
        right=mountainArr.length()-1

        while left<=right:

            mid=left+(right-left)//2
            midval=mountainArr.get(mid)
            if midval==target:
                return mid
            elif midval<target:
                right=mid-1
            else:
                left=mid+1
        return -1

        


        