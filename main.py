import csv

# Sample data to insert into the person.csv file
sample_data = [
    {'id': '1', 'name': 'Alice', 'gender': 'F'},
    {'id': '2', 'name': 'Bob', 'gender': 'M'},
    {'id': '3', 'name': 'Charlie', 'gender': 'M'},
    {'id': '4', 'name': 'Diana', 'gender': 'F'}
]

# Define the path for the new CSV file
csv_file_path = 'person.csv'

# Writing sample data to the CSV file
with open(csv_file_path, mode='w', newline='') as file:
    # Define the fieldnames
    fieldnames = ['id', 'name', 'gender']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the rows
    for row in sample_data:
        writer.writerow(row)

csv_file_path
