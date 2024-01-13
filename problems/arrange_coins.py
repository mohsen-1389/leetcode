class Solution:
    def arrange_coins(self, n: int) -> int:
        i = 1
        while n >= i:   
            n = n - i
            i += 1
        return i-1 
        
print(Solution().arrange_coins(10))