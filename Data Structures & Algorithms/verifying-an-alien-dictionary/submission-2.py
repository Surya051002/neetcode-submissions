class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        hashmap={}
        for i in range(len(order)):
            hashmap[order[i]]=i
        
        pos=0
        while len(words)>0:
            if pos<len(words[0]):
                val=hashmap[words[0][pos]]
            else:
                words.pop(0)
                continue
            flag=False
            print(pos)
            i=1
            while i<len(words):
                if pos<len(words[i]) and hashmap[words[i][pos]]==val:
                    break
                if pos<len(words[i]) and hashmap[words[i][pos]]>val:
                    val=hashmap[words[i][pos]]
                    words.pop(i-1)
                    flag=True
                    continue

                else:
                    return False
                i+=1
            else:
                if flag:
                    return True
            pos+=1
            
        return True
