""" 
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.


"""


# my solution 
class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0 or n == 1: 
            return n


        t_0: int = 0 
        t_1: int = 1
        t_2: int = 1 
        arr: list = [t_0, t_1, t_2]
        t_n: int = sum(arr)

        if n == 2: 
            return 1

        if n > 2: 

            for i in range(3, n+1): 

                t_n = sum(arr)
                arr.pop(0)
                arr.append(t_n)

        return t_n


# Chat gpt solution - no list needed      

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: 
            return 0
        if n == 1 or n == 2: 
            return 1

        t0, t1, t2 = 0, 1, 1

        for _ in range(3, n + 1):
            t_next = t0 + t1 + t2
            t0, t1, t2 = t1, t2, t_next  # shift the window

        return t2