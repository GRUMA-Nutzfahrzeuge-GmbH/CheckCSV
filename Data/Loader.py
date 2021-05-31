import csv


def load_whitlist(path):
    '''
    Loads the Csv and organise it in a list
    :param path: the path where the csv is
    :return: the keys of the whitelist
    '''
    data_array = []
    temp = []
    with open(str(path), 'rU', encoding='cp850') as f:
        csvread = csv.reader(f)
        batch_data = list(csvread)
    for data in batch_data:
        data_array.append(data)

    # removes the first row (Description)
    data_array.pop(0)
    # fixes the problem that sometimes \n appears infront of true or false
    for data in data_array:
        if "false 2\\n" in str(data):
            array = str(data).split('\\n')

            for data_part in array:
                data_temp = []
                data_temp.append(data_part)
                temp.append(data_temp)
        else:
            temp.append(data)
    # fixes the rows as the '\n' appears int the descriptions
    fixed_array = build_lines(temp)

    # gets the keys for the later comparison
    whitlist = get_key(fixed_array)
    return whitlist


def build_lines(array):
    '''
    builds the rows
    :param array: the whole array with broken rows
    :return: fixed array with rows
    '''
    full_array = []
    temp = []
    check_string1 = "false 2"
    check_string2 = "true 2"
    check_string3 = "false 2\\"
    check_string4 = "true 2\\"
    for data in array:
        temp.append(data)
        if check_string1 in str(data) or check_string2 in str(data) or check_string3 in str(data) or check_string4 in str(data):
            full_array.append(temp)
            temp = []
    return full_array


def get_key(array):
    '''
    Gets the keys as a list for the comparison
    :param array: array with the rows as in the csv
    :return: all keys to compare with
    '''
    whitlist = []
    temp = []
    for data in array:
        key = data[0][0]
        new_key = str.split(key, ';')
        temp.append(new_key[0])
        temp.append(new_key[1])
        temp.append(new_key[2])
        whitlist.append(temp)
        temp = []
    return whitlist


def load_dif(path):
    '''
    Loads the Csv and organise it in a list
    :param path: the path where the csv is
    :return: the keys of the sysconf
    '''
    data_array = []
    temp = []
    with open(str(path), 'rU', encoding='cp850') as f:
        csvread = csv.reader(f)
        batch_data = list(csvread)
    for data in batch_data:
        data_array.append(data)
    # removes the first row (Description)
    data_array.pop(0)
    # fixes the problem that sometimes \n appears infront of true or false
    for data in data_array:
        if "true 2\\n" in str(data) or "false 2\\n" in str(data):
            array = str(data).split('\\n')
            data = []

            for data_part in array:
                data_temp = []
                data_temp.append(data_part)
                temp.append(data_temp)

        temp.append(data)

    # fixes the rows as the '\n' appears int the descriptions
    list_data = build_lines(temp)
    # removes all rows with identical is true
    check_list = get_check_list(list_data)
    # gets the keys for the later comparison
    keys = get_key(check_list)
    return keys


def get_check_list(array):
    '''
    removes all rows which have identical is true
    :param array: the list of rows
    :return: all rows where identical is false
    '''
    check_list = []
    check_string1 = "false 2"
    check_string2 = "false 2\\"
    for data in array:
        if check_string1 in str(data) or check_string2 in str(data):
            check_list.append(data)
    return check_list