class Solution(object):
    def getCommon(self, nums1, nums2) -> int:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        if len(nums1) > len(nums2):
            l = len(nums1)
            s = len(nums2)
        elif len(nums1) < len(nums2):
            l = len(nums2)
            s = len(nums1)
        else:
            l = s = len(nums1)

        for i in range(0, l):
            if i == s :
                return -1


            if nums1[i] == nums2[i]:
                return nums1[i]




a = Solution()
print(a.getCommon([1,2,3,4], [2,3]))
