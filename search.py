import sys
import csv

# Check input length
if len(sys.argv) != 2:
    print("Usage: python3 search.py <name>")
    sys.exit(1)

# Get name from input
search_name = sys.argv[1]

try:
    with open('person.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        # iterate through rows
        for row in reader:
            if row['name'] == search_name:
                print(row)
except Exception as e:
    print(f"An error occurred: {e}")
