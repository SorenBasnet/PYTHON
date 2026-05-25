class Solution(object):
    def fizzBuzz(self, n):

        output = []

        for j in range(0, n):

            i = j + 1

            if ((i % 3) == 0 and (i % 5) == 0):
                output.append("FizzBuzz")
            elif ((i % 3) == 0):
                output.append("Fizz")
            elif ((i % 5) == 0):
                output.append("Buzz")
            else:
                output.append(i)

        return(output)



fb = Solution()
print(fb.fizzBuzz(3))


