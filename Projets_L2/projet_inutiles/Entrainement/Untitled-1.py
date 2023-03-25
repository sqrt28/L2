print(2)

def nombres_paire():
    l = []
    for i in range(10):
        if i % 2 == 0:
            l.append(i)
    return l
print(nombres_paire())