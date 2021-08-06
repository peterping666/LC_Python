class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in dic:
                return (dic[num], i)
            else:
                dic[target - num] = i
        return ()
