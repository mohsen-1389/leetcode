class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        sorted_score = sorted(score, reverse=True)
        result = []
        for item in score:
            index = sorted_score.index(item)
            index += 1
            if index == 1:
                result.append('Gold Medal')
            elif index == 2:
                result.append('Silver Medal')
            elif index == 3:
                result.append('Bronze Medal')
            else:
                result.append(str(index))
            
        return result
    
print(Solution().findRelativeRanks([10,3,8,9,4]))