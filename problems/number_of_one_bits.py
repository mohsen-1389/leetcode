class Solution:
    def hammingWeight(self, n: int) -> int:
        n = format(n, 'b')
        ones = 0
        for i in n:
            if i == '1':
                ones = ones+1
            
        return ones
print(Solution().hammingWeight(678))    