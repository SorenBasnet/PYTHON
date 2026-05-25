
class Solution(object):
    def numberOfArithmeticSlices(self, List: nums):

        if len(nums) < 3:
            return 0

        count = 0
        total = 0

        for i in range(2, len(nums)):

            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                count += 1
                total += count
            else:
                count = 0

        return total











