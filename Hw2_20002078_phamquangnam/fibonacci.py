import sys
import argparse
import time

def finbonacci_recursion(n: int) -> int:
    if n < 2:
        return n
    else: 
        return finbonacci_recursion(n - 1) + finbonacci_recursion(n - 2)

def fibonacci(n: int) -> int:
    while not n < 2:
        idx = 1
        temp_0 = 0
        temp_1 = 1
        temp = 0
        while idx < n:    
            temp = temp_0 + temp_1
            temp_0 = temp_1
            temp_1 = temp 
            idx += 1
        return temp
    
    return n   
   
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int)
    args = parser.parse_args()
    start = time.time()
    print(finbonacci_recursion(args.n))
    end = time.time()
    print(f'Total time excute: {end - start}')
    
    start = time.time()
    print(fibonacci(args.n))
    end = time.time()
    print(f"Total time excute: {end - start}")
    