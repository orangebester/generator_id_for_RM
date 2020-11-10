
import random
import xlsxwriter
import pandas as pd


alphabet = list('abcdefghijklmnopqrstuvwxyz')
data = pd.read_excel(r'C:/Users/Xiaomi/Downloads/data_release_table.xlsx', engine='openpyxl')
storage_for_check = list(data["id"])
workbook = xlsxwriter.Workbook("New_ID.xlsx")
worksheet = workbook.add_worksheet()
bold = workbook.add_format({"bold": True})
worksheet.write(0, 0, "Новий ID:", bold)


def generate_n_id(n):
    storage = []
    row, col = (1, 0)
    for step in range(n):
        first = random.randint(0,9)
        second = "a"
        third = "a"
        forth = "a"
        fifth = random.randint(0,1)
        final_id = str(first)
        if final_id not in storage and final_id not in storage_for_check:
            storage.append(final_id)
            worksheet.write(row, col, final_id)
            row += 1
        elif final_id in storage or final_id in storage_for_check:
            generate_id()
    print(storage)


def generate_id():
    first = random.randint(0,9)
    second = "a"
    third = "a"
    forth = "a"
    fifth = random.randint(0,1)
    final_id = str(first)
    return final_id


generate_n_id(8)
workbook.close()
