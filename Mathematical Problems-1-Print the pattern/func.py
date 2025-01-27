class Solution:
    def printPat(self, n):
        return sum([([i for i in range(n, 0, -1) for j in range(n - k)] + [-1]) for k in range(n)], [])


