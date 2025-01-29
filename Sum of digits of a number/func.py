class Solution:
    def isDigitSumPalindrome(self, n):
        dig_sum = str(sum(int(d) for d in str(n)))
        return dig_sum == dig_sum[::-1]