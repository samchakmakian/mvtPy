import csv
from astropy.time import Time


def timeconv(intime):
    # MJD date string
    mjd_date = intime

    # Convert MJD date to Astropy Time object
    mjd_time = Time(mjd_date, format='mjd', scale='utc')

    # Fermi's Mission Elapsed Time Origin (MET0)
    fermi_met0 = Time('2001-01-01T00:00:00.000', format='isot', scale='utc')

    # Calculate the time difference
    time_diff = mjd_time - fermi_met0

    # Convert time difference to Fermi MET (1 MET = 1 second)
    fermi_met = time_diff.sec

    return fermi_met


# Read times from input CSV file
input_file = input('csv file with unconverted times:')
output_file = 'trigtimeconverted.csv'

times = []

with open(input_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header if present
    for row in reader:'Converted Time (Fermi MET)'
        if row:  # Check if row is not empty
            times.append(row[0])

# Convert times using timeconv function
converted_times = [timeconv(time) for time in times]

# Round converted times to 3 digits after the decimal point
rounded_times = [round(time, 3) for time in converted_times]

# Write rounded converted times to output CSV file
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['trig_time'])
    for rounded_time in rounded_times:
        writer.writerow([rounded_time])

print("Conversion complete. Converted times saved to", output_file)
