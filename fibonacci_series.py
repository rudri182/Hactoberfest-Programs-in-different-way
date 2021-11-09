import numpy as np

def fibonacci_series(n, method="analytical"):
    solvers = {
        "analytical": analytical_fibonacci_series,
        "recursive": recursive_fibonnaci_series
    }
    if method not in solvers.keys():
        raise Exception("The method provided must be one of " + ", ".join(solvers.keys()))
    return solvers[method](n)
    

def analytical_fibonacci_series(n):
    alpha = np.divide(1+np.sqrt(5),2)
    beta = np.divide(1-np.sqrt(5),2)
    return int(np.divide(alpha**n-beta**n,np.sqrt(5)) + .5) # Use rounding to avoid floating point errors

def recursive_fibonnaci_series(n, f_0=0, f_1=1):
    assert (n>=0 and type(n) == int)
    if n==0:
        return f_0
    else:
        return recursive_fibonnaci_series(n-1, f_0 = f_0 + f_1, f_1 = f_0)
