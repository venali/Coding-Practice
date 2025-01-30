class Solution:
    def kthDigit(self, A, B, K):
        # code here
        res=A**B
        st=str(res)
        if K>len(st):
            return 0
        return int(st[-K])
