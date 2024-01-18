import textgrid
import csv
import numpy as np
import pandas as pd

# Path to your TextGrid file
file_path = '/Users/anandderick/College/CORINA LAB RESEARCH /speech1_chunk0.TextGrid'

# Load the TextGrid file
tg = textgrid.TextGrid.fromFile(file_path)


print(type(tg)) 
#prints the types of data avalible in TextGrid file

for tier in tg.tiers:
    print("Tier name:", tier.name) 

phones_tier = None
for tier in tg.tiers:
    if tier.name == "phones":
        phones_tier = tier
        break

# Check if the 'phones' tier was found
#if phones_tier is not None:
    # Iterate over intervals in the 'phones' tier and print them
 #   for interval in phones_tier:
  #      print(interval.minTime, interval.maxTime, interval.mark)
#else:
 #   print("The 'phones' tier was not found in the TextGrid file.")

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



print("There are ",counter,"ARPABets which have numbers attached to it")

# Specify the CSV file name
csv_file_path = '/Users/anandderick/College/CORINA LAB RESEARCH /step1.csv'

# Write the matrix to a CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write the header row if desired
    csvwriter.writerow(['Start Time', 'End Time', 'ARPABet'])
    # Write the data rows
    csvwriter.writerows(interval_matrix)

print(f"Data successfully exported to {csv_file_path}")



# Load the CSV file
df = pd.read_csv(csv_file_path)

# Removing any numbers from the ARPABet column
df['ARPABet'] = df['ARPABet'].str.replace(r'\d', '', regex=True)

# Save the modified dataframe back to a CSV file
modified_file_path = '/Users/anandderick/College/CORINA LAB RESEARCH /step2.csv'
print(f"Data successfully exported to {modified_file_path}")
df.to_csv(modified_file_path, index=False)

#print(df)

df = pd.read_csv('/Users/anandderick/College/CORINA LAB RESEARCH /step2.csv')

df['Start Time'] = round(df['Start Time']*128)
df['End Time'] = round(df['End Time']*128)

#print(df)
min_start_time = int(df['Start Time'].min())
max_end_time = int(df['End Time'].max())

results = []
min_start_time = int(df['Start Time'].min())
max_end_time = int(df['End Time'].max())

for num in range(min_start_time, max_end_time + 1):
    interval = df[(df['Start Time'] <= num) & (df['End Time'] > num)]
    if not interval.empty:
        results.append((num, interval.iloc[0]['ARPABet']))
    else:
        results.append((num, np.nan))

result_df = pd.DataFrame(results, columns=['Hertz', 'ARPABet'])

# Define the output file path on your local machine
output_file_path = '/Users/anandderick/College/CORINA LAB RESEARCH /step3.csv'

# Export the DataFrame to a CSV file
result_df.to_csv(output_file_path, index=False)

print(f"Data  successfully exported to {output_file_path}")

df = pd.read_csv('/Users/anandderick/College/CORINA LAB RESEARCH /step3.csv')


# Summarize the data: count the occurrences of each ARPABet
arpabet_counts = df['ARPABet'].value_counts()

# Convert the summary to a DataFrame
summary_df = pd.DataFrame({'ARPABet': arpabet_counts.index, 'Count': arpabet_counts.values})

# Define the output file path for the summary
summary_output_file_path = '/Users/anandderick/College/CORINA LAB RESEARCH /summary.csv'  # Replace with your desired output path

# Export the summary DataFrame to a CSV file
summary_df.to_csv(summary_output_file_path, index=False)

print(f"Summary data successfully exported to {summary_output_file_path}")
#################################################################################################

import pandas as pd

# Load the CSV file
file_path = '/Users/anandderick/College/CORINA LAB RESEARCH /step3.csv'  # Replace with your CSV file path
  # Replace with your actual file path
df = pd.read_csv(file_path)

# Create dummy columns for each unique ARPABet
pivot_df = pd.get_dummies(df, columns=['ARPABet'])

# Group by 'Hertz' and sum the dummies
pivot_df = pivot_df.groupby('Hertz').sum()

# Reset the index to make 'Hertz' a column again
pivot_df.reset_index(inplace=True)

# Export to CSV
output_csv = '/Users/anandderick/College/CORINA LAB RESEARCH /step4.csv'  # Replace with your desired output file path
pivot_df.to_csv(output_csv, index=False)

print("Conversion complete. Data exported to", output_csv)

