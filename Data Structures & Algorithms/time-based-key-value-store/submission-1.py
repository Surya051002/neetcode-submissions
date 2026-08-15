class TimeMap:

    def __init__(self):
        self.hashmap={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].append([value,timestamp])
        else:
            self.hashmap[key]=[]
            self.hashmap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        
 
        if not key in self.hashmap: return ""
        l=self.hashmap[key]
        left=0
        right=len(l)-1
        while left<=right:

            mid=left+(right-left)//2

            if l[mid][1]==timestamp:
                return l[mid][0]
            if l[mid][1]>timestamp:
                right=mid-1
            else:
                left=mid+1
        if l[right][1]<=timestamp:
            return l[right][0]
        return ""
