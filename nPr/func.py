class Solution:
    def nPr(self, n, r):
        # code here
        def fact(a):
            f = 1
            for i in range(a, 1, -1):
                f = f*i
            return f
        
        npr = fact(n) // fact(n-r)
        return npr