import requests
import random
import xlsxwriter


alphabet = list('abcdefghijklmnopqrstuvwxyz')
workbook = xlsxwriter.Workbook("New_ID.xlsx")
bold = workbook.add_format({"bold": True})


def generate_n_id(n):
    temp_storage = []
    while len(temp_storage) < n:
        final_id = generate_id()
        response = requests.get('https://www.renovationmap.org/building/'+ final_id)
        if final_id not in temp_storage and response.status_code != 200:
            temp_storage.append(final_id)
    return temp_storage


def generate_id():
    first = random.randint(0,9)
    second = random.choice(alphabet)
    third = random.choice(alphabet)
    forth = random.choice(alphabet)
    fifth = random.randint(0,9)
    not_final_id = str(first) + second.upper() + third + forth.upper() + str(fifth)
    return not_final_id


def general_func(n):
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, "Новий ID:", bold)
    final_storage = generate_n_id(n)
    for i, element in enumerate(final_storage, start = 2):
        worksheet.write(f'A{i}', element)


general_func(2)
workbook.close()