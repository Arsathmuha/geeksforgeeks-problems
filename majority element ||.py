from collections import Counter
class Solution:
    def findMajority(self, arr):
        n=len(arr)
        limit=n//3
        
        count=Counter(arr)
        
        result=[]
        
        for num in count:
            if count[num]>limit:
                result.append(num)
        result.sort()
                
                
        return result
