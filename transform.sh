#!/bin/bash

# Default conditions for awk, sed, and cut
awk_condition='$3 > 30'       # Default: filter rows where age > 30
sed_condition='s/San Francisco/SF/g'   # Default: replace "San Francisco" with "SF"
cut_fields='2,4'              # Default: select name and city fields (2 and 4)
output_file=""

# Parse options using getopts
while getopts "a:s:c:o:" opt; do
  case $opt in
    a) awk_condition="$OPTARG" ;;  # Custom awk condition
    s) sed_condition="$OPTARG" ;;  # Custom sed replacement
    c) cut_fields="$OPTARG" ;;     # Custom cut fields
    o) output_file="$OPTARG" ;;    # Custom output file
    *) 
       echo "Usage: $0 [-a awk_condition] [-s sed_condition] [-c cut_fields] [-o output_file] <path-to-file>"
       exit 1
       ;;
  esac
done

# Shift the parsed options away, so the file path remains as the last argument
shift $((OPTIND - 1))

# Check if the file path is provided
if [ -z "$1" ]; then
  echo "Usage: $0 [-a awk_condition] [-s sed_condition] [-c cut_fields] [-o output_file] <path-to-file>"
  exit 1
fi

# Set input file
input_file="$1"

# Set default output file name if none is provided
if [ -z "$output_file" ]; then
  output_file="transformed_$(basename "$input_file")"
fi

# Temporary files
temp_file=$(mktemp)
filtered_file=$(mktemp)

# Step 1: Apply the awk filter (skipping header row)
awk -F, "NR==1{next} $awk_condition" "$input_file" > "$filtered_file"

# Step 2: Apply the sed transformation
sed "$sed_condition" "$filtered_file" > "$temp_file"

# Step 3: Extract specified fields with cut and add header row
{
  echo "name,city"  # Adding a static header row (customizable if needed)
  cut -d ',' -f "$cut_fields" "$temp_file"
} > "$output_file"

# Cleanup temporary files
rm "$temp_file" "$filtered_file"

# Notify the user
echo "Transformation complete. Output saved to $output_file"
