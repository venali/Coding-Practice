class Solution:
    def closestNumber(self, n , m):
        q = N // M
        # closest value to M
        m1 = q* M
        m2 = (q + 1) * M
        
        # Compare distances to determine the closest multiple
        if abs(N - m1) < abs(N - m2):
            return m1
        elif abs(N -m2) < abs(N - m1):
            return m2
        else:
            # If distances are equal, return the one with greater absolute value
            return m1 if abs(m1) > abs(m2) else m2
