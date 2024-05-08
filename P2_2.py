import csv
import time
from datetime import datetime

# 1
with open('r_200.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["№", "Секунда", "Микросекунда"])

    for i in range(1, 201):
        now = datetime.now()
        writer.writerow([i, now.second, now.microsecond])
        time.sleep(0.02)

# 2
import os


def print_directory_contents(path):
    for dirpath, dirnames, filenames in os.walk(path):
        print(f'Opening directory: {dirpath}')
        for filename in filenames:
            print(filename)


# Replace 'your_directory_path' with the path of the directory you want to print
print_directory_contents("C:\\Users\\daota\\Documents")
print("--------------------------------------------------------")


# 3

def print_words_by_length(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        words = file.read().split()
    words.sort(key=len, reverse=True)
    for word in words:
        print(word)


print_words_by_length('text.txt')
print("--------------------------------------------------------")

# 4
import csv

# Step 1: Create a .csv file
with open('file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Header1", "Header2", "Header3"])  # Header
    writer.writerow(["Data1", "Data2", "Data3"])  # Data row
    writer.writerow(["Data4", "Data5", "Data6"])  # Data row

# Step 2: Read the .csv file
with open('file.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Header
    rows = list(reader)  # Data rows

print("Header:", header)
print("Rows:", rows)