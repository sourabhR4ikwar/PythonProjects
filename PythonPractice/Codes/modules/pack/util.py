def find_max(list):
    max = list[0]
    for item in range(len(list)):
        if list[item] > max:
            max = list[item]

    return max;
