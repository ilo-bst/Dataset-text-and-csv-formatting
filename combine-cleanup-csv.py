# This script combines all csv files in the directory "Datasets",
# deleting the rows containing "Pronunciation,Latex".
# The combined csv file is saved to combined.csv in the directory "Datasets". 

import os
import pandas as pd

# Define the directory containing the .csv files
directory = 'Datasets'

# Initialize an empty list to store individual DataFrames
data = []

# Process each .csv file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)
        
        try:
            # Read the content from the .csv file
            df = pd.read_csv(file_path)
            data.append(df)

        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except Exception as e:
            print(f"An error occurred while processing '{file_path}': {e}")

# Combine all DataFrames into a single DataFrame
combined_df = pd.concat(data, ignore_index=True)

# Remove rows containing "Pronunciation,Latex"
combined_df = combined_df[~combined_df.apply(lambda row: row.astype(str).str.contains("Pronunciation,Latex").any(), axis=1)]

# Define the path for the combined CSV file
combined_csv_file_path = os.path.join(directory, 'combined.csv')

# Save the combined DataFrame to a CSV file
try:
    combined_df.to_csv(combined_csv_file_path, index=False)
    print(f"Combined CSV file '{combined_csv_file_path}' has been created.")
except Exception as e:
    print(f"An error occurred while creating the combined CSV file: {e}")
