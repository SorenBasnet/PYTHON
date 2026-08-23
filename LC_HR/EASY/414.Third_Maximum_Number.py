
class Solution(object):

    def thirdMax(self, nums):

        nums.sort()

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return nums[1]

        frequencies = {}

        for j in range(len(nums),0, -1):

            if j != 0:


                i = j - 1

                if (nums[i] in frequencies):
                    pass
                else:
                    frequencies[nums[i]] = 1

        #sorted_frequencies = sorted(frequencies, key=frequencies.get, reverse=True)

        if len(frequencies) == 2:
            return(frequencies[len(frequencies) - 1])

        return(frequencies[2])


tm = Solution()
print(tm.thirdMax([1,3,2,3]))






