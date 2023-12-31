class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        number = int(''.join(str(digit) for digit in digits))
        number += 1
        number_str = str(number)
        result = [int(digit) for digit in number_str]
        return result
             
print(Solution().plusOne([9]))