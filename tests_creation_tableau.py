def tableau(n):
    liste = []
    a = 1
    for i in range(n):
        liste.append([a+j+i for j in range(n)])
        a+=2
    return liste

print(tableau(3))

def tableau2(n):
    return [[i for i in range(n)]for j in range(n)]
print(tableau2(3))
            