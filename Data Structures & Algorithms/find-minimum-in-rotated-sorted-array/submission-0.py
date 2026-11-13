class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + (r - 1))//2
            if nums[mid] < nums[r]: # peak could be at right side
                r = mid
            else: #  peak at right
                l = mid + 1
        return nums[l]
        