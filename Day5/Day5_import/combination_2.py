n = 5
r = 3

def combination(selected):
    if len(selected) == r:
        print(selected)
        return
    
    max_value = 0
    if selected:
        max_value = selected[-1]

    for i in range(max_value + 1, 6):
        selected.append(i)
        combination(selected)
        selected.pop()

combination([])