def change_money(A, T):
    k = [0] * len(A)
    for i in range(0, len(A)):
        k[i] = 0
        i = 0
        while (i < len(A) and T > 0):
            k[i] = T // A[i]
            print(f'the value of k[i] = {k[i]}')
            T -= k[i] * A[i]
            i += 1
        if ( T > 0):
            return -1
        else:
            return k
    
if __name__ == "__main__":
    A = [1, 5, 10, 50]
    T = 78
    A = sorted(A, reverse=True)
    solution = change_money(A, T)
    print(f'solution of problem: ', solution)