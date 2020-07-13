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


def sort_by_age(student_list):
    cities = {s['city'] for s in student_list}
    sorted_dict = {c: [] for c in cities}
    for s in student_list:
        sorted_dict[s['city']].append({k: v for k, v in s.items() if k != 'city'})
    print(sorted_dict)
    return sorted_dict


# ЛИСТ ДЛЯ ПЯТОЙ ФУНКЦИИ
students_list = [
        {'name': 'Viktor', 'age': 30, 'city': 'Kiev'},
        {'name': 'Andrey', 'age': 34, 'city': 'Kiev'},
        {'name': 'Maksim', 'age': 20, 'city': 'Dnepr'},
        {'name': 'Artem', 'age': 50, 'city': 'Dnepr'},
        {'name': 'Vladimir', 'age': 32, 'city': 'Lviv'},
        {'name': 'Dmitriy', 'age': 21, 'city': 'Lviv'}]

# ДИКТ ДЛЯ ЧЕТВЕРТОЙ ФУНКЦИИ
diction1 = {'name': 'Viktor', 'age': 30, 'city': 'Kiev'}
diction2 = {'name': 'Viktor', 'age': 50, 'city': 'Kiev'}

# ЛИСТ ДЛЯ ПЕРВОЙ, ВТОРОЙ И ТРЕТЬЕЙ ФУНКЦИЙ
n_list = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]

# ПЕРВАЯ ФУНКЦИЯ
three_biggest_int(n_list)
# ВТОРАЯ ФУНКЦИЯ
reversed_list(n_list)
# ТРЕТЬЯ ФУНКЦИЯ
lowest_int_index(n_list)
# ЧЕТВЕРТАЯ ФУНКИЯ
common_key = find_common_keys(diction1, diction2)
print(common_key)
# ПЯТАЯ ФУНКЦИЯ
sort_by_age(students_list)
