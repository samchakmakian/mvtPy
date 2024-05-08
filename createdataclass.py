from dataclasses import dataclass
import csv


@dataclass
class GRB:
    name: str
    t0: float
    t90: float


# Read data from CSV and convert it into RowData instances
def read_csv(filename):
    rows = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row_data = GRB(row['name'], row['trig_time'], row['t90'])
            rows.append(row_data)
    return rows


# Function to return t0 for a given GRB
def return_t0(rows, target_name):
    for grb in rows:
        if grb.name == target_name:
            return grb.t0 # Stop searching after finding the matching GRB
    print("GRB with name", target_name, "not found.")


# Function to return t90 for a given GRB
def return_t90(rows, target_name):
    for grb in rows:
        if grb.name == target_name:
            return grb.t90 # Stop searching after finding the matching GRB
    print("GRB with name", target_name, "not found.")


# Example usage:
# csv_filename = 'nametrigt90.csv'
# rows = read_csv(csv_filename)
# target_grb_name = input('Target GRB to print t0 and t90:\n')
# print_t0_for_grb(rows, target_grb_name)
# print_t90_for_grb(rows, target_grb_name)
