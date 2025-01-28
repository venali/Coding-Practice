#code
no_of_test_case = int(input())
for iter in range (no_of_test_case):
    number = int(input())
    for i in range(1,10):
        print(number*i,end=' ')
    print(number*10)
