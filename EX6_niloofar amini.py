# exercise 6: part A: fibonacci:

def fib (n):
    if n==1 or n==2:
        return 1
    return fib (n-1)+ fib (n-2)


# exercise 6: part B:

def fibonacci(n):

 if n == 0:
    fibonacci_list = []
 elif n == 1:
    fibonacci_list = [1]
 elif n == 2:
    fibonacci_list = [1, 1]
 elif n > 2:
    fibonacci_list = [1, 1]
    for i in range(n-2):
        fibonacci_list += [0]
        fibonacci_list[-1] = fibonacci_list[-2] + fibonacci_list[-3]
 return fibonacci_list







                   



            









