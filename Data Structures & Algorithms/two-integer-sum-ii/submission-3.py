class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(numbers)):
            remainder = target - numbers[i]
            if mp[remainder]:
                return [mp[remainder], i + 1]
            mp[numbers[i]] = i + 1
        return []
