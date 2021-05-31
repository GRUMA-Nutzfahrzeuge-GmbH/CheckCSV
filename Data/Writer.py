import csv


def write_csv(list, name='finished'):
    '''
    Writes list in an csv
    :param list:the list which should be written in the csv
    :return:
    '''
    with open(name+'.csv', 'w', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(list)
