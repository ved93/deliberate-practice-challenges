


def calc(n):
    operations_count = [0] * (n + 1)

    operations_count[1] = 1
    for i in range(2, n + 1):
        count_index = [i - 1]
        if i % 2 == 0:
            count_index.append(i // 2)
        if i % 3 == 0:
            count_index.append(i // 3)

        # print(count_index)
        

        min_count = min([operations_count[x] for x in count_index])

        # print(count_index, [operations_count[x] for x in count_index])

        operations_count[i] = min_count + 1
    # print(operations_count)

    current_value = n
    value_trail = [current_value]
    while current_value != 1:
        option_list = [current_value - 1]
        if current_value % 2 == 0:
            option_list.append(current_value // 2)
        if current_value % 3 == 0:
            option_list.append(current_value // 3)

        current_value = min([(c, operations_count[c]) for c in option_list], key=lambda x: x[1])[0]
        value_trail.append(current_value)
    print(value_trail)
    return reversed(value_trail)



if __name__ =='__main__':
    # input = sys.stdin.read()
    # n = int(input)
    # sequence = list(fast_optimal_sequence(n))
    # print(len(sequence) - 1)
    print(calc(99))
