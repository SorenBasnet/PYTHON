class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        total = sum(nums)

        if total % 2 != 0:
            return False

        dp = {0}

        for num in nums:


            new_dp = set(dp)

            for s in dp:
                new_dp.add(s + num)

            dp = new_dp

        return total//2 in dp



