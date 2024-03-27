import sys
import csv

# Check input length
if len(sys.argv) != 4:
    print("Usage: python3 insert.py <id> <name> <gender>")
    sys.exit(1)

# Get id, name, gender from input
record_id, name, gender = sys.argv[1], sys.argv[2], sys.argv[3]

# Check input validation
if gender not in ['M', 'F']:
    print("Gender must be 'M' or 'F'.")
    sys.exit(1)

# Check if ID is an integer
if not record_id.isdigit():
    print("ID must be an integer.")
    sys.exit(1)

try:
    with open('person.csv', mode='r+', newline='') as file:
        # Read CSV
        reader = csv.DictReader(file)
        existing_ids = [row['id'] for row in reader]

        # Check ID
        if record_id in existing_ids:
            print("Error: ID already exists.")
        else:
            file.seek(0,2)
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(['id', 'name', 'gender'])
            writer.writerow([record_id, name, gender])
except Exception as e:
    print(f"An error occurred: {e}")