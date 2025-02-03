nCr
Difficulty: MediumAccuracy: 14.82%Submissions: 315K+Points: 4
Given two integer values n and r, the task is to find the value of Binomial Coefficient nCr

A binomial coefficient nCr can be defined as the coefficient of x^r in the expansion of (1 + x)^n.
A binomial coefficient nCr also gives the number of ways, disregarding order, that r objects can be chosen from among n objects more formally, the number of r-element subsets (or r-combinations) of a n-element set.
Note: If r is greater than n, return 0.

Examples:

Input: n = 3, r = 2
Output: 3
Explaination: 3C2 = 3. 
Input: n = 2, r = 4
Output: 0
Explaination: r is greater than n.
Input: n = 5, r = 0
Output: 1
Explaination: Any nC0 = 1 by definition, regardless of the value of nn.
Constraints:
1 ≤ n ≤ 33
1 ≤ r ≤ 32