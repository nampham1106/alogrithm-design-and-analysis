import sys
import argparse
import time

def binary_number_recursion(n: int) -> str:
    if n ==  0:
        return ""
    else: 
        return binary_number_recursion(n//2) + str(n % 2)

def binary_number(n: int) -> str:
    while not n == 0:
        temp = ""
        while n != 0:
            temp = str(n % 2) + temp            
            n = n // 2
        return temp
    return ""
   
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int)
    args = parser.parse_args()
    start = time.time()
    print(binary_number_recursion(args.n))
    end = time.time()
    print(f'Total time excute: {end - start}')
    
    start = time.time()
    print(binary_number(args.n))
    end = time.time()
    print(f"Total time excute: {end - start}")
    