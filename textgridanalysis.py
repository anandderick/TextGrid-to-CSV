import textgrid
import csv

# Path to your TextGrid file
file_path = 'Yourfile/textgridfile.TextGrid'

# Load the TextGrid file
tg = textgrid.TextGrid.fromFile(file_path)


print(type(tg)) 

for tier in tg.tiers:
    print("Tier name:", tier.name) 

phones_tier = None
for tier in tg.tiers:
    if tier.name == "phones":
        phones_tier = tier
        break

# Check if the 'phones' tier was found
if phones_tier is not None:
    # Iterate over intervals in the 'phones' tier and print them
    for interval in phones_tier:
        print(interval.minTime, interval.maxTime, interval.mark)
else:
    print("The 'phones' tier was not found in the TextGrid file.")

# Initialize an empty list to hold all intervals
interval_matrix = []

# Find the 'phones' tier and extract intervals
for tier in tg.tiers:
    if tier.name == "phones":
        for interval in tier:
            # Create a list for the current interval and append it to the matrix
            interval_matrix.append([interval.minTime, interval.maxTime, interval.mark])

# Now 'interval_matrix' contains the data in a format that can be written to a CSV file

counter = 0
#I want to see how many phones are blank
for tier in tg.tiers:
    if tier.name == "phones":
        for interval in tier:
            if interval.mark == "":
                counter=counter+1



print(counter)

# Specify the CSV file name
csv_file_path = '/Users/anandderick/College/CORINA LAB RESEARCH /phones_intervals.csv'

# Write the matrix to a CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write the header row if desired
    csvwriter.writerow(['Start Time', 'End Time', 'ARPABet'])
    # Write the data rows
    csvwriter.writerows(interval_matrix)

print(f"Data exported to {csv_file_path} successfully.")

