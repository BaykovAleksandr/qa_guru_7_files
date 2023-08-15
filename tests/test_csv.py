import csv
import os
from conftest import RESOURCES_DIR

# TODO оформить в тест, добавить ассерты и использовать универсальный путь


with open(os.path.join(RESOURCES_DIR, 'new_csv.csv'), 'w', newline='') as csv_file:
    csvwriter = csv.writer(csv_file, delimiter=';')
    csvwriter.writerow(['Bonny', 'Born', 'Peter'])
    csvwriter.writerow(['Alex', 'Serj', 'Yana'])

with open(os.path.join(RESOURCES_DIR, 'new_csv.csv')) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=';')
    result = []
    for row in csvreader:
        result.append(row)
        print(row)

    assert result[0] == ['Bonny', 'Born', 'Peter']
    assert result[1] == ['Alex', 'Serj', 'Yana']

os.remove(os.path.join(RESOURCES_DIR, 'new_csv.csv'))