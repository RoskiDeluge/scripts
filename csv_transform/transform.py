#!/usr/bin/env python3
import csv
import argparse
import os
import re
from typing import List, Dict

def transform_csv(
    input_file: str,
    output_file: str = None,
    awk_condition: str = '$3 > 30',
    sed_condition: str = 's/San Francisco/SF/g',
    cut_fields: str = '2,4'
) -> None:
    # Set default output file if none provided
    if not output_file:
        output_file = f"transformed_{os.path.basename(input_file)}"
    
    # Convert cut fields to list of integers (1-based to 0-based indexing)
    field_indices = [int(f) - 1 for f in cut_fields.split(',')]
    
    # Parse sed-style replacement
    pattern = sed_condition.split('/')[1]
    replacement = sed_condition.split('/')[2]
    
    # Parse awk-style condition
    awk_field = int(awk_condition.split('$')[1].split()[0]) - 1
    awk_value = int(awk_condition.split('>')[1].strip())
    
    transformed_data: List[Dict] = []
    
    # Read and transform the CSV
    with open(input_file, 'r') as infile:
        reader = csv.reader(infile)
        next(reader)  # Skip header row
        
        for row in reader:
            # Apply awk-style filtering
            if float(row[awk_field]) > awk_value:
                # Apply sed-style replacement
                row = [re.sub(pattern, replacement, field) for field in row]
                # Select specified fields
                selected_fields = [row[i] for i in field_indices]
                transformed_data.append(selected_fields)
    
    # Write transformed data with new header
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['name', 'city'])  # Write header
        writer.writerows(transformed_data)
    
    print(f"Transformation complete. Output saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Transform CSV files')
    parser.add_argument('input_file', help='Input CSV file path')
    parser.add_argument('-o', '--output', help='Output file path')
    parser.add_argument('-a', '--awk', default='$3 > 30', help='AWK-style condition')
    parser.add_argument('-s', '--sed', default='s/San Francisco/SF/g', help='SED-style replacement')
    parser.add_argument('-c', '--cut', default='2,4', help='Cut fields (comma-separated)')
    
    args = parser.parse_args()
    
    transform_csv(
        args.input_file,
        args.output,
        args.awk,
        args.sed,
        args.cut
    )

if __name__ == '__main__':
    main()
