# Dataset-text-and-csv-formatting

This is part of a bigger project that generates and formats datasets in a specified form. This repository contains scripts to combine individual TXT files into a CSV file and perform other dataset formatting tasks.

## Overview

The scripts in this repository perform the following tasks:
1. Combine all TXT files in a specified directory into a single TXT file.
2. Convert the combined TXT file into a CSV file.
3. Combine all CSV files in a specified directory into a single CSV file while removing specific unwanted rows.

## Scripts

### 1. combine-txt-csv.py

This script combines all `.txt` files in the `txt-files` directory into a single `combined.txt` file and converts it into a `combined.csv` file.

### 2. combine-cleanup-csv.py

This script combines all `.csv` files in the `Datasets` directory into a single `combined.csv` file while removing all lines containing "Pronunciation,Latex".

## Usage

1. Ensure you have the required directories (`txt-files` and `Datasets`) in the same location as the scripts.
2. Run the scripts using Python:
    ```sh
    python combine-txt-csv.py
    python combine-cleanup-csv.py
    ```

## Cleanup

To delete all `.csv` files in the `txt-files` directory for cleanup, you can use the following command:

### For Windows Command Prompt:
```sh
del txt-files\*.csv
```

### For Unix-like Systems (Linux, MacOS):
```sh
rm txt-files/*.csv
```


