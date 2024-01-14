class Solution:
    def reverse_str(self, s: str, k: int) -> str:
        def reverse_sub_str(k, item):
            return item[:k][::-1] + item[k:]

        result = ""
        split = [s[i:i + 2*k] for i in range(0, len(s), 2*k)]
        for item in split[0:len(split)]:
            if len(item) < 2*k and len(item) >= k:
                reverse_sub = reverse_sub_str(k, split[-1])
                result = result + reverse_sub
            elif len(item) < k:
                reverse_sub = split[-1][::-1]
                result = result + reverse_sub
            else:
                reverse_sub = reverse_sub_str(k, item)
                result = result + reverse_sub
            
        return result
        
print(Solution().reverse_str("abcdefg", 2))