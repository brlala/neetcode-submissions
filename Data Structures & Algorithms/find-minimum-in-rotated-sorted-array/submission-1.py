class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + (r - 1))//2
            if nums[mid] < nums[r]: # min at left side, cut off all right
                r = mid
            else: #  min at right
                l = mid + 1
        return nums[l]
        