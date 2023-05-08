# def towerHanoi(n, from_rod, to_rod, aux_rod):
#     if n == 0:
#         return
#     towerHanoi(n - 1, from_rod, aux_rod, to_rod)
#     print('Move disk', n, 'from rod', from_rod, 'to rod', to_rod)
#     print(n)
#     towerHanoi(n - 1, aux_rod, to_rod, from_rod)
#
#
# N = 3
# towerHanoi(N, 'A', 'C', 'B')


# def hanoi(n, start, end):
#     if n == 1:
#         pm(start, end)
#     else:
#         other = 6 - (start + end)
#         print(other)
#         hanoi(n - 1, start, other)
#         pm(start, end)
#         hanoi(n - 1, other, end)
#
#
# def pm(start, end):
#     print(start, '->', end)


# hanoi(3, 1, 3)


# def pretty_print_numbers(numbers):
#     if numbers < 10:
#         print(numbers)
#     else:
#         print(numbers)
#         pretty_print_numbers(numbers // 10)
#         print(numbers)
#
#
# pretty_print_numbers(4003)

# def rec(s):
#     if len(s) == 1 or len(s) == 2:
#         return s
#     return s[0] + '(' + rec(s[1:-1]) + ')' + s[-1]
#
#
# s = input()
# print(rec(s))


# def power(x, n):
#     if n == 0:
#         return 1
#     if n < 0:
#         return 1 / power(x, -n)
#     if n % 2 == 0:
#         return power(x, n // 2) * power(x, n // 2)
#     else:
#         return power(x, n - 1) * x
#
#
# x = int(input())
# n = int(input())
# print(power(x, n))


a = [1, [3, [4, [3, 4]], [2, 3, [4]]], 2, [2, 3, 4, [3, 4, [2, 3], 5]]]


def rec(lists, level=1):
    print(*lists, 'level=', level)
    for i in lists:
        if type(i) is list:
            rec(i, level + 1)


rec(a)