def shellSort(input_list, n):
    gap = n // 2
    while gap > 0:
        j = gap
        while j < n:
            i = j - gap
            while i >= 0:
                if input_list[i + gap] > input_list[i]:
                    break
                else:
                    input_list[i + gap], input_list[i] = input_list[i], input_list[i + gap]
                i = i - gap
            j += 1
        gap = gap // 2


list = [19, 2, 31, 45, 30, 11, 121, 27]
shellSort(list, len(list))
print(list)
