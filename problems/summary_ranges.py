class Solution:
    def summary_ranges(self, nums: list[int]) -> list[str]:
        result_list = []
        start_sub_list = 0
        for i, _ in enumerate(nums):
            if nums[i] != nums[-1]:
                if nums[i] + 1 == nums[i+1]:
                    continue
                else:
                    if nums[start_sub_list]!= nums[i]:
                        result_list.append(f"{nums[start_sub_list]}->{nums[i]}")
                    else:
                        result_list.append(f"{nums[i]}")
                    start_sub_list = i+1
            else:
                if nums[i] == nums[i-1] + 1:
                    if nums[start_sub_list]!= nums[i]:
                        result_list.append(f"{nums[start_sub_list]}->{nums[i]}")
                    else:
                        result_list.append(f"{nums[i]}")
                else:
                    result_list.append(f"{nums[-1]}")
        return result_list
                    
    
print(Solution().summary_ranges([0,1,2,4,5,7]))