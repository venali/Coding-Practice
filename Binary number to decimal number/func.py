class Solution:
    def binaryToDecimal(self, b):
        count=0
        s=0
        st=b
        st=st[::-1]
        for i in st:
            s+=int(i)*pow(2,count)
            count+=1
        return s