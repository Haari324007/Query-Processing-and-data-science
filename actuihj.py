import csv
import re

def main():
    csv_file = 'user_data.csv'

    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row_number, row in enumerate(reader, start=2):
            name, email, password, age = row

            if not re.match(r'^[A-Za-z\s]+$', name):
                print(f"Row {row_number}: Invalid name")
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                print(f"Row {row_number}: Invalid email")
            if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$', password):
                print(f"Row {row_number}: Invalid password")
            if not re.match(r'^[1-9][0-9]$', age):
                print(f"Row {row_number}: Invalid age")
            if all(re.match(r'^[A-Za-z\s]+$', field) or re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', field) or re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$', field) or re.match(r'^[1-9][0-9]$', field) for field in row):
                print(f"Row {row_number}: Valid")

if __name__ == "__main__":
    main()
