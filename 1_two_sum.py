class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return (dic[num], i)
            else:
                dic[target - num] = i
        return []