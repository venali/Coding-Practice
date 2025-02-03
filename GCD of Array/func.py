import math
class Solution:
    def gcd(self, n, arr):
        if n == 1 :
            return arr[0]
        ans = arr[0]
        for num in arr :
            ans = math.gcd(ans,num)
        return ans