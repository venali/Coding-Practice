class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        # code here
        prod=a*b
        while(a>0 and b>0):
            if a>b: a=a%b
            else: b=b%a
        gcd=int(a) if b==0 else int(b)
        lcm=int(prod/gcd)
        
        return [lcm,gcd]
