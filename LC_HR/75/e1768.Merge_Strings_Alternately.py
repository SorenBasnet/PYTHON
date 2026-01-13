"""
You are given two strings word1 and word2. 
Merge the strings by adding letters in 
alternating order, starting with word1. 
If a string is longer than the other, 
append the additional letters onto the 
end of the merged string.

Return the merged string.
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        shorter_length_string: str = min(word1, word2, key=len)
        shorter_length: int = len(shorter_length_string) # O(1)
        longer_string: int = max(word1, word2, key=len) # O(1)
        merged_string: str = ""

        for i in range(0, shorter_length-1):  # O(m2)
            merged_string += word1[i] # O(current_length_of_merged_string) and i do it twice so 
                                      # its O(m2)
            merged_string += word2[i]

        
        longer_string = longer_string[shorter_length-1:]  # O(n − m) : A brand new string is created.

        merged_string += longer_string #O(n) : Copies everything into a new string

        return merged_string

        



solution = Solution() 
print(solution.mergeAlternately("abcd", "pq"))



# ----------------------
# --------------------- 


# Optimal soltion 

class Solution2: 

    def mergeAlternatively(self, word1: str, word2:str) -> str:

        res: list= []
        i: int = 0 

        while i < len(word1) or i < len(word2): 
            if i < len(word1): 
                res.append(word1[i])

            if i < len(word2): 
                res.append(word2[i]) # O(1) appending to list is O(1)

            i += 1

        return ''.join(res) # O(total length) i.e. O(n + m)