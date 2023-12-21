n = 5
r = 3

def permutaion(selected):
    if len(selected) == r:
        print(selected)
        return

    for i in range(1, n + 1):
        if i not in selected:
            selected.append(i)
            permutaion(selected)
            selected.pop()

permutaion([])