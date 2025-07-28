class Solution:
    def maximumProfit(self, prices):
        mp=float('inf')
        maxp=0
        
        for price in prices:
            if price<mp:
                mp=price
            else:
                p=mp-price
                
                if p>maxp:
                    maxp=p:
        return maxp
