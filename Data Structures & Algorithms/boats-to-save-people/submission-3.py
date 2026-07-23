class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n=len(people)
        i=0
        j=n-1
        ans=0
        while i<=j:
            ans+=1
            if(people[j]+people[i]<=limit):
                i+=1
            j-=1
        return ans

            

            
            
        