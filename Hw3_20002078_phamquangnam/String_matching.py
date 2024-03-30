def string_matching(P, T):
    result  = []
    for i in range(len(T)-len(P)+1):
        if T[i:i+len(P)] == P:
            result.append(i)
    return result

f1 = open("./input.txt", "r")
f2 = open("./output.txt", "w")

T = f1.readline()
P = "favorite movie star"

result = string_matching(P, T)
for i in result:
    f2.write(str(i) + " ")
    