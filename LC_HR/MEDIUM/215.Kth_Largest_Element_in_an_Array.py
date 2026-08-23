

class Solution(object):

    def findKthLargest(self, num, k):

        num.sort()  # O(n logn)

        return num[len(num)-k]




solution = Solution()

print(solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4))


