#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            if not isinstance(my_list_1[i], (int, float)) or not isinstance(my_list_2[i], (int, float)):
                print("wrong type")
                new_list.append(0)
                continue

            if my_list_2[i] == 0:
                print("division by 0")
                new_list.append(0)
                continue
            result = my_list_1[i] / my_list_2[i]
            new_list.append(result)
        except IndexError:
            print("out of range")
            break

    return new_list
