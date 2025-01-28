no_of_trials = int(input())
for iter in range(no_of_trials):
    first_term,second_term = map(int,input().split())
    nth_term = int(input())
    ratio = second_term/first_term
    term = first_term*(ratio**(nth_term-1))
    print(int(term))