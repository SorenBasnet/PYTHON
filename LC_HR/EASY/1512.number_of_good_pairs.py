class Solution(object):

    def numIdenticalPairs(self, nums):

        #count = 0

        #for i in range(0, len(nums)):

        #    if i != len(nums)-1:
        #        for j in range(i+1, len(nums)):

        #            if nums[i] == nums[j]:
        #                count += 1

        #print(count)

        count = 0
        frequencies = {}

        for num in nums:

            if num in frequencies:
                count += frequencies[num]
                frequencies[num] += 1
            else:
                frequencies[num] = 1

        return count


identical = Solution()
print(identical.numIdenticalPairs([1,2,1]))
