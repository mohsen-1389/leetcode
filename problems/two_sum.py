class Solution:
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sum_dict = {}
        for i, item in enumerate(nums):
            if (target - item) in sum_dict.values():
                 return [list(sum_dict.keys())[list(sum_dict.values()).index((target - item))], i]
            else:
                sum_dict[i] = item
                
           
            
            
print(Solution().twoSum(nums=[2,7,11,15], target=9))