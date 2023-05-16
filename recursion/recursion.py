def rec(lists, level=1):
    print(*lists, 'level = ', level)
    for i in lists:
        if type(i) is list:
            rec(i, level + 1)


a = [1, [3, [4, [3, 4]], [2, 3, [4]]], 2, [2, 3, 4, [3, 4, [2, 3], 5]]]
rec(a)