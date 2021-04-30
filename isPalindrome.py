class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = ""
        x = str(x)
        for i in reversed(x):
            reverse += i
        return reverse == str(x)