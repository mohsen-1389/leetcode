class Solution:
    def romanToInt(self, s: str) -> int:
        mapping_rules = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
             'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0
        for i, _ in enumerate(s):
            if i+1 <= len(s) -1 and s[i:i+2] in mapping_rules.keys():     
               sum = sum + mapping_rules[s[i:i+2]]
               i = i+2
            else:
                sum = sum + mapping_rules[s[i]]
                i = i+1
        return sum
        
print(Solution().romanToInt('MCMXCIV'))