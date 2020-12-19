import requests
import sys
import random
import json


alphabet = list('abcdefghijklmnopqrstuvwxyz')


def generate_n_id(n):
    """ And checks whether generated id is unique """
    temp_storage = []
    while len(temp_storage) < n:
        final_id = generate_id()
        response = requests.get(
            'https://www.renovationmap.org/building/' + final_id)
        if final_id not in temp_storage and response.status_code != 200:
            temp_storage.append(final_id)
    return temp_storage


def generate_id():
    """ Generates id each elements of which consist of random values """
    first = random.randint(0, 9)
    second = random.choice(alphabet)
    third = random.choice(alphabet)
    forth = random.choice(alphabet)
    fifth = random.randint(0, 9)
    not_final_id = str(first) + second.upper() + \
        third + forth.upper() + str(fifth)
    return not_final_id


def general_func(n):
    """ Write results of a script in json/txt file """
    file1 = sys.argv[2]
    if file1.endswith('.txt'):
        final_storage = generate_n_id(n)
        with open(file1, "w") as file2:
            file2.write("Новий ID: \n")
            for element in final_storage:
                file2.writelines(element+"\n")
    elif file1.endswith('.json'):
        final_storage = dict(enumerate(generate_n_id(n), start=1))
        with open(file1, "w") as file2:
            json.dump(final_storage, file2)
    else:
        print('Extension of a file is incorrect.\nPlease use file, which extension is ".json" or ".text"')
        sys.exit()


general_func(int(sys.argv[1]))
