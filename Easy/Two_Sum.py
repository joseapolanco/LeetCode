from typing import List

#  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.



# This inital solution worked and although used a bit less memory it took much longer due to it having a complexity of O(n²)
# More often than not we can sacrifice using more memory if it will produce a shorter runtime.

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         length = range(len(nums))
#         for x in length:
#             for y in length:
#                 if x != y and nums[x]+nums[y] == target:
#                     return [x,y]


# When running a program with a O(n²) it can most likely be improved by using a map/dictionary to reduce it to O(n) at the cost of memory also being O(n). 
# Below is the solution with the improved method of using a dicitonary to store the value we subtracted from the target value if the number needed for the sum to equal the target is not already present in the map/dicitionary

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for x in range(len(nums)):
            need_num = target - nums[x]
            if myMap.get(need_num) != None:
                return [x, myMap.get(need_num)]
            else:
                myMap.update({nums[x]: x})



# solution = Solution()
# my_list = [2,7,11,15]
# my_target = 9

# print(solution.twoSum(my_list, my_target))








