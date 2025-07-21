class Solution:
	def pushZerosToEnd(self,arr):
    	write=0
    	
    	for i in range(len(arr)):
    	    if arr[i]!=0:
    	        arr[write]=arr[i]
    	        write+=1
    	        
    	while write<len(arr):
    	    arr[write]=0
    	    write+=1
    	    
    	return arr
