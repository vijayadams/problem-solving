class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}
        for idx,val in enumerate(nums):
            nums_map[val] = idx
        
        for idx,val in enumerate(nums):
            target_needed = target - val
            if(target_needed in nums_map and nums_map[target_needed] != idx):
                return [idx,nums_map[target_needed]]