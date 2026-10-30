# 07_csv_file.py

import csv

# Open the CSV file
with open("student-data.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    # Read and display every row
    for row in reader:
        print(row)
