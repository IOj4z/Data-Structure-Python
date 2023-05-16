def insertion_sort(inputList):
    for i in range(1, len(inputList)):
        j = i - 1
        nxt_element = inputList[i]
    while (inputList[j] > nxt_element) and (j >= 0):
        inputList[j + 1] = inputList[j]
        j = j - 1
        inputList[j + 1] = inputList[j]


list = [19, 2, 31, 45, 30, 11, 121, 27]
insertion_sort(list)
print(list)
