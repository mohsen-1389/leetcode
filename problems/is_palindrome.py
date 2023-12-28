class Solution:
    # Solution 1:
    # converting integer to string
    def is_palindrome_by_int_to_str(self, x: int) -> bool:
        num_to_str = str(x)
        for i, digit in enumerate(num_to_str):
            if num_to_str[i] != num_to_str[len(num_to_str) - 1 - i]:
                return False
        return True
            
    
print(Solution().is_palindrome_by_int_to_str(0))