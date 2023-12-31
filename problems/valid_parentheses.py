class Solution:
    
    def isValid(self, s: str) -> bool:
        stack = []
        char_dict = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for char in s:
            if char in {'(', '{', '['}:
                stack.append(char)
            elif char in {')', '}', ']'}:
                if len(stack) == 0:
                    return False
                else:
                    top = stack.pop()
                    if char_dict[top] != char:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False
    
    
    
print(Solution().isValid('[)'))    