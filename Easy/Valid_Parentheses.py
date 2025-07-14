# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.



# class Solution:
#     def isValid(self, s: str) -> bool:
#         tempString = ""
#         parenthesesMap = {")":"(","}":"{","]":"["}

#         if len(s) == 1:
#             return False

#         for parentheses in s:
#             if parentheses == "(" or parentheses == "{" or parentheses == "[":
#                 tempString += parentheses
#             elif len(tempString) == 0 and (parentheses == ")" or parentheses == "}" or parentheses == "]"):
#                 return False
#             else:
#                 if tempString[-1] != parenthesesMap.get(parentheses):
#                     return False
#                 else:
#                     tempString = tempString[:-1]

#         return tempString == ""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesesMap = {")":"(","}":"{","]":"["}

        for parentheses in s:
            if parentheses == "(" or parentheses == "{" or parentheses == "[":
                stack.append(parentheses)
            elif len(stack) == 0 and (parentheses == ")" or parentheses == "}" or parentheses == "]"):
                return False
            else:
                if stack[-1] != parenthesesMap.get(parentheses):
                    return False
                else:
                    stack.pop()

        return not stack


s = "()[]{}"

solution = Solution()
print(solution.isValid(s))