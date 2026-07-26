class Solution:
    def isValid(self, s: str) -> bool:
        stack = ""
        bracket_pairs = {'(' : ')', '[' : ']' , '{' : '}'}
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack += i
            else:
                if len(stack) == 0:
                    return False
                if bracket_pairs[stack[-1]] != i:
                    return False
                else:
                    stack = stack[:-1]
        return not bool(stack)