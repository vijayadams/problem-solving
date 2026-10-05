class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueElements = set()

        for num in nums:
            if num in uniqueElements:
                return True
            else:
                uniqueElements.add(num)
        return False