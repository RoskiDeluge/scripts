# CSV Transform Script

A flexible CSV transformation script that allows filtering, text replacement, and column selection from CSV files.

## Usage

```bash
./transform.sh [-a awk_condition] [-s sed_condition] [-c cut_fields] [-o output_file] <path-to-file>
```

Options: 

-a : AWK condition for filtering rows (default: $3 > 30) \
-s : SED pattern for text replacement (default: s/San Francisco/SF/g) \
-c : Columns to extract (default: 2,4) \
-o : Output filename (default: transformed_<input-filename>)

Examples:

1. Basic usage with default settings:

```bash
./transform.sh data.csv
```

2. Filter rows where age is greater than 25:
```bash
./transform.sh -a '$3 > 25' data.csv
```

3. Replace "New York" with "NY":
```bash
./transform.sh -s 's/New York/NY/g' data.csv
```

4. Select specific columns (1,3,5):
```bash
./transform.sh -c '1,3,5' data.csv
```

5. Specify output file:
```bash
./transform.sh -o processed_data.csv data.csv
```

6. Comine all options:
```bash
./transform.sh -a '$3 > 25' -s 's/New York/NY/g' -c '1,3,5' -o processed_data.csv data.csv
```

Output:
- The script creates a new CSV file with the transformed data
- Default output filename: transformed_<input-filename>
- Header row is automatically added: "name,city"

Notes:
- Input CSV must be comma-separated
- The script preserves the first row (header) during filtering
- Temporary files are automatically cleaned up after processing
