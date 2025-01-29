class Solution:
    def armstrongNumber (self, n):
        # code here 
    
        rem=0
        rev = 0
        op=n
        while n>0 :
            rem = n%10
            c = rem**3
            rev = rev+c
            n= n//10
        if rev == op:
            return True
        else:
            return False
