class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)

        for idx,val in enumerate(nums):
            if(idx == 0):
                continue
            elif nums[idx-1] == nums[idx]:
                return True
        return False