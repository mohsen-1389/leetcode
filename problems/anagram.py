class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        if len(s) == len(t):
            for index, _ in enumerate(s):
                if s[index] in list(dict_s.keys()):
                    dict_s[s[index] ] += 1
                else:
                    dict_s[s[index] ] = 1
                if t[index] in list(dict_t.keys()):
                    dict_t[t[index] ] += 1
                else:
                    dict_t[t[index]] = 1 
            if dict_s == dict_t:
                return True
            else:
                return False
        else:
            return False
        
print(Solution().isAnagram('anagram', 'nagaram'))