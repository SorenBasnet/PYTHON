class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if len(nums) == k:
            return max(nums)


        count = [0] * 51

        for i in nums:
            count[i] += 1

        if k == 1:
            for i in range(len(count), -1, -1):
                if count[i] == 1:
                    return i

            return -1

        else:
            if count[len(nums)] == 1:
                return len(nums)
            elif count[0] == 1:
                return 0
            else:
                return -1




