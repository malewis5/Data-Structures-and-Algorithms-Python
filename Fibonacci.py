## Iterative Solution ##

def iterFibonacci(n):
  if n < 0:
    return ValueError('Number must be positive.')
  fibs_list = [0,1]
  if n <= len(fibs_list) - 1:
    return fibs_list[n]
  else:
    while n > len(fibs_list) - 1:
      next_fib = fibs_list[-1] + fibs_list[-2]
      fibs_list.append(next_fib)
  return fibs_list[n]
      
  


# test cases
print(iterFibonacci(3) == 2)
print(iterFibonacci(7) == 13)
print(iterFibonacci(0) == 0)
print(iterFibonacci(-1))

## Recursive Solution ##

def recFibonacci(n):
  if n < 0:
    ValueError("Input 0 or greater only!")
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)

print(recFibonacci(3))
print(recFibonacci(7))
print(recFibonacci(0))
