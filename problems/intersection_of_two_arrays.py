class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1).intersection(set(nums2)))
    
print(Solution().intersection([4,9,5], [9,4,9,8,4]))