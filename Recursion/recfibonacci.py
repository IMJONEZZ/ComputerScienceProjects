def fibonacci(n):
  # base cases
  if n == 1:
    print("Recursive call with 1 as input")
    return n
  if n == 0:
    print("Recursive call with 0 as input")
    return n
  
  # recursive step
  print("Recursive call with {0} as input".format(n))
  return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(30)
# set the appropriate runtime:
# 1, logN, N, N^2, 2^N, N!
fibonacci_runtime = "2^N"
