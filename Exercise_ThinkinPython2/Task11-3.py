'''Memoize the Ackermann function from Exercise 6.2 and see if memoization
makes it possible to evaluate the function with bigger arguments. Hint: no.

Grabbed to original version to work of from!
'''

def ackermann(m, n):
    """Computes the Ackermann function A(m, n)
    See http://en.wikipedia.org/wiki/Ackermann_function
    n, m: non-negative integers
    """
    
    global memo
        
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    
    if (m, n) in memo:
        return memo[(m, n)]
    
    res = ackermann(m-1, ackermann(m, n-1))
    memo[(m, n)] = res
    return res

memo = {}

print(ackermann(2,4))
print(memo)