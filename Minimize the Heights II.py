class Solution:
    def getMinDiff(self,arr,k):
        n=len(arr)
        
        arr.sort()
        
        ans=arr[n-1] - arr[0]
        
        for i in range(1,n):
            if arr[i] - k<0:
                continue
            
            min_height = min(arr[0]+ k, arr[i] - k)
            max_height=max(arr[i-1] + k, arr[n-1] - k)
            
            ans = min(ans, max_height - min_height)
            
        return ans
