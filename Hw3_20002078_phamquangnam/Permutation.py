def permutation(i, arr, used, order):
    if i == len(arr):
        print(" ".join(order))
        return

    for j in range(len(arr)):
        if not used[j]:
            used[j] = True
            order[i] = arr[j]
            permutation(i + 1, arr, used, order)
            used[j] = False

if __name__ == "__main__":
    n = int(input("Nhap vao do dai cua to hop: "))
    print('\nNhap vao phan tu cua to hop by line: ')
    arr = [input() for _ in range(n)]
    used = [False] * n
    order = [''] * n
    print("output: ")
    permutation(0, arr, used, order)
