class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # corner case
        if not nums:
            return []

        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0 or left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                elif sum > 0 or right < len(nums) - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
        return res