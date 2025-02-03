from fractions import Fraction

def addFraction(num1, den1, num2, den2):
    #Code here
    # from fractions import Fraction
    n = (num1*den2)+(num2*den1)
    d = den1*den2
    value = n/d
    return print(Fraction(value).limit_denominator())
