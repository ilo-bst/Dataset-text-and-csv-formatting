import os
import csv

# Define the directory containing the .txt files
directory = 'txt-files'

# Initialize an empty list to store all lines from all .txt files
all_lines = []

# Process each .txt file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        input_file_path = os.path.join(directory, filename)
        
        try:
            # Read the content from the .txt file
            with open(input_file_path, 'r', encoding='utf-8') as file:
                text_content = file.read()

            # Split the text content into lines
            lines = text_content.strip().split('\n')
            all_lines.extend(lines)

        except FileNotFoundError:
            print(f"Error: The file '{input_file_path}' was not found.")
        except Exception as e:
            print(f"An error occurred while processing '{input_file_path}': {e}")

# Combine all lines into a single .txt file
combined_txt_file_path = os.path.join(directory, 'combined.txt')
try:
    with open(combined_txt_file_path, 'w', encoding='utf-8') as combined_file:
        for line in all_lines:
            combined_file.write(line + '\n')
    print(f"Combined text file '{combined_txt_file_path}' has been created.")
except Exception as e:
    print(f"An error occurred while creating the combined text file: {e}")

# Convert the combined .txt file to a CSV file
combined_csv_file_path = os.path.join(directory, 'combined.csv')
try:
    with open(combined_txt_file_path, 'r', encoding='utf-8') as file:
        combined_text_content = file.read()

    combined_lines = combined_text_content.strip().split('\n')

    with open(combined_csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        for line in combined_lines:
            columns = line.split(',', 1)
            csv_writer.writerow(columns)

    print(f"Combined CSV file '{combined_csv_file_path}' has been created.")
except Exception as e:
    print(f"An error occurred while creating the combined CSV file: {e}")
