# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

from typing import List



# First solution I made
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         strs.sort()
#         mappedWord = {}
#         prefix = ""

#         print(strs)

#         if len(strs) == 0:
#             return prefix
#         elif len(strs) == 1:
#             return "".join(list(mappedWord.values()))
#         else:
#             smallestLength = len(strs[0])

#         for word in strs:
#             if len(word) < smallestLength:
#                 smallestLength = len(word)
        
#         for index in range(smallestLength):
#             mappedWord.update({index : strs[0][index]})

#         print(mappedWord)
        
#         lastWord = strs[len(strs) - 1]

#         for index in range(smallestLength):
#             if lastWord[index] == mappedWord.get(index):
#                 prefix += lastWord[index]
#             else:
#                 break
                
#         return prefix




# Improved version of my first solution after reflecting on the best solution shown
# Overall would be better to just assume the first word is the prefix and then trim it while comparing
# it to every word in the list.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        prefix = ""

        if len(strs) == 0:
            return prefix
        elif len(strs) == 1:
            return "".join(strs)
        
        firstWord,lastWord = strs[0], strs[-1]

        for index in range(len(firstWord)):
            if firstWord[index] == lastWord[index]:
                prefix += firstWord[index]
            else:
                break
                
        return prefix





solution = Solution()

myList = ["cir","car"]
print(solution.longestCommonPrefix(myList))