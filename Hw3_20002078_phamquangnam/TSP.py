import os
import numpy as np

adjacency_matrix = np.array([[0, 10, 15, 20],
                    [10, 0, 35, 25],
                    [15, 35, 0, 30],
                    [20, 25, 30, 0]])

print(adjacency_matrix)

N = 4

Cmin = np.ma.masked_equal(adjacency_matrix, 0, copy=False).min()
print(Cmin)

best_cost = np.inf
sum = 0
print(best_cost)
cost = 0
flags = [0] * N

print(flags)


print("after algorithms: ")
def BB(i: int, sum, best_cost):
    xi = 1
    for j in range(2, N):
        if flags[j] == 0:
            xi = j 
            flags[j] = 1
            sum = sum + adjacency_matrix[xi - 1, xi]
            g = sum + (N - 1 + 1) * Cmin
            print("The value of i: ", i)
            if (i == 3):
                cost = sum + adjacency_matrix[N - 1, 0]
                print("cost value: ", cost)
                if cost <= best_cost:
                    best_cost = cost
            else: 
                if g <= best_cost:
                    BB(i + 1, sum, best_cost)
            sum = sum - adjacency_matrix[xi - 1, xi]
            flags[j] = 0
BB(0,sum, best_cost)