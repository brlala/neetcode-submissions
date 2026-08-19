class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # using maps
        mp = defaultdict(int)
        for i in range(len(numbers)):
            remainder = target - numbers[i]
            if mp[remainder]:
                return [mp[remainder], i + 1]
            mp[numbers[i]] = i + 1
        return []

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # using two pointers
        l, r = 0, len(numbers) - 1
        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum == target:
                return [l+1, r+1]
            elif currSum > target:
                r -= 1
            else:
                l += 1
        return []
