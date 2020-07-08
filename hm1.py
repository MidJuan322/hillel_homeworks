def catalog_finder(url_list):
    result_list = list(filter(lambda x: '/catalog/' in x, url_list))
    return result_list


def get_str_center(input_str):
    mid = len(input_str) // 2
    if len(input_str) % 2 == 0:
        output_str = input_str[mid - 1:mid + 2]
        return output_str
    else:
        print('Что-то пошло не так!')


def count_symbols(input_str):
    output_dict = {}
    for symb in input_str:
        output_dict[symb] = output_dict.get(symb, 0) + 1
    return output_dict


def mix_strings(str1, str2):
    a = len(str1) // 2
    result_str = f'{str1[:a]}{str2}{str1[a:]}'
    return result_str


def even_int_generator():
    even_int_list = list(i for i in range(100) if not i % 2)
    return even_int_list

