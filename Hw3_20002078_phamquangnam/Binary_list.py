def binary_list_n(n, i, text, result):
    for b in ['0', '1']:
        if i == n:
            result.append(text)
            return
        else:
            binary_list_n(n, i+1, text+b, result)
            
def binary_list(n):
    l = []
    binary_list_n(n, 0, '', l)
    return l

n = int(input("Nhap so n la chieu dai day nhi phan: "))
l = binary_list(n)
for i in l:
    print(i + "\n")