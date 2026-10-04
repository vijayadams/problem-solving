from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        window = deque()
        result = []

        for right in range(len(nums)):

            # 1. Remove indices that are outside the window
            while window and window[0] <= right - k:
                window.popleft()

            # 2. Remove smaller elements from the right
            #    because they can never become the maximum
            while window and nums[window[-1]] <= nums[right]:
                window.pop()

            # 3. Add current index
            window.append(right)

            # 4. Once we have a complete window,
            #    the first index has the maximum value
            if right >= k - 1:
                result.append(nums[window[0]])

        return result