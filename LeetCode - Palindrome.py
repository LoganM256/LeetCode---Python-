class Solution(object):

    def isPalindrome(self, x):
        string_form = str(x)
        reversed_string = string_form[::-1]
        if reversed_string == string_form:
            return True
        else:
            return False

testcase1 = Solution()
testcase2 = Solution()
testcase3 = Solution()

print(testcase1.isPalindrome(121))
print(testcase1.isPalindrome(-121))
print(testcase1.isPalindrome(10))
    