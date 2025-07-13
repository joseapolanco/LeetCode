# Given an integer x, return true if x is a palindrome, and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1

import time

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        xLength = len(x) - 1

        for index in range(xLength):
            if x[index] != x[xLength - index]:
                return False

        return True

start = time.perf_counter_ns()

solution = Solution()
print(solution.isPalindrome(1000021))

end = time.perf_counter_ns()

print(f"Execution time: {end - start} nanoseconds")




# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         x = str(x)
#         print(x[::-1])


# solution = Solution()
# solution.isPalindrome(12345)