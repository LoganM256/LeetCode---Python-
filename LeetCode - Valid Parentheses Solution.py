class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {'(':')', '{':'}', '[':']'}
        stack = []

        for item in s:
            if item in mapping:
                stack.append(item)
            elif len(stack) == 0 or mapping[stack.pop()] != item:
                return False
        
        return len(stack) == 0
