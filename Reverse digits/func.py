class Solution:
    def reverseDigits(self, n):
        n_str = str(n)  # "120"
        reversed_str = n_str[::-1]  # "021"
        reversed_n = int(reversed_str)  # 21 (leading zero is discarded)
        return reversed_n