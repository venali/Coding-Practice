class Solution:
    def gcd(self, a : int, b : int) -> int:
        # code here
        if (b == 0):
            return a
        return self.gcd(b, a%b)