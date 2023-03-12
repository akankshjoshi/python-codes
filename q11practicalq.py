def min_value(list):
    min = list[0]
    for i in list:
        if i<min:
            min = i
    return min

num = [12,65,44,32,77,88,99,21]
print(min_value(num))