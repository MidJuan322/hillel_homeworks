def three_biggest_int(input_list):
    print(*sorted(input_list)[:3])
    return three_biggest_int


def lowest_int_index(input_list):
    index = min(range(len(input_list)), key=lambda i: (input_list[i], -i))
    print(index)
    return lowest_int_index


def reversed_list(input_list):
    l = len(input_list)
    for i in range(l // 2):
        input_list[i], input_list[l - 1 - i] = input_list[l - 1 - i], input_list[i]
    print(input_list)
    return reversed_list


def find_common_keys(dict1, dict2):
    common_keys = {}
    for key, value in dict1.items():
        if key in dict2 and value == dict2[key]:
            common_keys[key] = value
    return common_keys


dict1 = {'name': 'Viktor', 'age': 30, 'city': 'Kiev'}
dict2 = {'name': 'Viktor', 'age': 50, 'city': 'Kiev'}
list = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]

three_biggest_int(list)

reversed_list(list)

lowest_int_index(list)

common_key = find_common_keys(dict1, dict2)
print(common_key)

