no_of_trail = int(input())
for iter in range(no_of_trail):
    first_term,second_term = map(int,input().split())
    nth_term = int(input())
    differnce = second_term-first_term
    term = first_term + (nth_term-1)*differnce
    print(term)