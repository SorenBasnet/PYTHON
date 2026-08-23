class Solution:
    def merge(self, nums1, m, nums2, n) -> None:

        #for i in range(0, len(nums1)):
        #    if nums1[i] == 0:
        #        nums1.pop(i)

        del nums1[n:m]



        nums1 = nums1 + nums2
        nums1.sort()

        return nums1


m = Solution()

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

print(m.merge(nums1, len(nums1), nums2, len(nums2)))

