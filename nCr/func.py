class Solution:
    def nCr(self, n, r):
        # code here
        if r>n:
            return 0
        def fac(x):
            if x==0 or x==1:
                return 1
            return x*fac(x-1)
            
        x=fac(n)//(fac(r)*fac(n-r))
        return x