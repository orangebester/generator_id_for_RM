
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
    temp_storage = []
    while len(temp_storage) < n:
        first = random.randint(0,9)
        second = random.choice(alphabet)
        third = random.choice(alphabet)
        forth = random.choice(alphabet)
        fifth = random.randint(0,9)
        final_id = str(first) + second.upper() + third + forth.upper() + str(fifth)
        if final_id not in temp_storage and final_id not in storage_for_check:
            temp_storage.append(final_id)
    return temp_storage


def main(n):
    final_storage = generate_n_id(n)
    row, col = (1, 0)
    for element in final_storage:
        worksheet.write(row, col, element)
        row += 1



main(5)
workbook.close()