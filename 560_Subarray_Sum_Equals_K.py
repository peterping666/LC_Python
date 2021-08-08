class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        pre_sum = {0:1}
        sum = 0
        res = 0
        for i in range(len(nums)):
            sum += nums[i]
            res += pre_sum.get(sum - k, 0)
            pre_sum[sum] = pre_sum.get(sum, 0) + 1
        return res