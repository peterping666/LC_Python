# Space O(n)
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [nums[0]]
        res = dp[0]
        for i in range(1, len(nums)):
            dp.append(max(nums[i], dp[i - 1] + nums[i]))
            res = max(res, dp[i])
        return res

# Space O(1)
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = dp = nums[0]
        for i in range(1, len(nums)):
            dp = max(nums[i], dp + nums[i])
            res = max(res, dp)
        return res

