class Solution:
    def isHappy(self, n: int) -> bool:
        def get_digits(n):
            res = []
            while n >= 1:
                res.append(n % 10)
                n = n // 10
            return res
        # Loop over for 10 times, if didn't find happy number in 10 step, return false
        for _ in range(210):
            digits = get_digits(n)
            sum_square_of_digits = 0
            for digit in digits:
                sum_square_of_digits += digit**2
            print(sum_square_of_digits)
            if sum_square_of_digits == 1:
                return True
            else:
                n = sum_square_of_digits
                continue
        return False
    
print(Solution().isHappy(2))