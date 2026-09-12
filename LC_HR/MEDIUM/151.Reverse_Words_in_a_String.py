
class Solution:

    def reverseWords(self, s: str) -> str:

        string = s.split()
        reverse = ""

        for i in range(len(string), 0, -1):

            reverse += string[i-1]

            if i-1 != 0:
                reverse += " "

        return reverse


a = Solution()
print(a.reverseWords("Hello World"))


