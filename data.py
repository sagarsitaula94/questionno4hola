import csv

def store_array_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Example usage
data = [
    [1, 'John', 'Doe'],
    [2, 'Jane', 'Smith'],
    [3, 'Bob', 'Johnson']
]
filename = 'data.csv'
store_array_to_csv(data, filename)
print(f"Data stored in '{filename}' successfully.")
