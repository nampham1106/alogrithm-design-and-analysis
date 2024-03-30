def knapsack(A, T):
    S = [0] * 5
    for i in range(len(A)):
        i = 0
        while (i < len(A) and T > 0):
            S[i] = T // A[i][1]   
            print(S[i], A[i][1])
            T -= S[i] * A[i][1]
            i += 1
        if (T > 0):
            return -1
        else:
            return S 

if __name__ == "__main__":
    # maps: {(price, kg): name}
    maps = {
        (4, 12):1, 
        (2, 1):2,
        (10, 4):3,
        (1, 1):4,
        (2, 2):5,
        }
    T = 15
    values = sorted(maps.keys(), key=lambda item: item[0], reverse=True)
    print(f'items: {values}')
    solution = knapsack(values, T)
    print(f'solution: {solution}')
    print(f'price: {sum([solution[i] * keys[0] for i,keys in enumerate(maps.keys())])}')