# DataDB: Data File to SQLite Database Converter

`datadb.py` is a command-line utility for easily importing and exporting data between various file formats and a SQLite database.

## Features

- **Import data** from `.csv`, `.json`, and `.xlsx` files into a SQLite database.
- **Export data** from a SQLite table to `.csv`, `.json`, and `.xlsx` files.
- **Flexible table handling**: Choose to replace, append, or fail if the table already exists.
- **Customizable**: Specify database and table names.

## Requirements

- Python 3
- pandas
- openpyxl (for Excel support)

## Installation

1.  **Clone the repository or download the script.**
2.  **Install the required libraries:**

    ```bash
    pip install pandas openpyxl
    ```

## Usage

The script can be run from the command line with various arguments to control its behavior.

### General Syntax

```bash
python datadb.py [file_path] [options]
```

### Arguments

-   `file_path`: (Required) The path to the input or output file.
-   `-t`, `--table_name`: The name of the SQL table. If not provided, the file name (without extension) is used.
-   `-d`, `--db_name`: The name of the SQLite database. Defaults to `main.db`.
-   `-e`, `--if_exists`: Action to take if the table already exists.
    -   `replace`: Drop the table before inserting new values.
    -   `append`: Insert new values into the existing table.
    -   `fail`: Do nothing if the table exists.
-   `-x`, `--export`: Export mode. Use this flag to export a table from the database to a file.

### Examples

#### Importing Data

-   **Import a CSV file into the default database (`main.db`) and a table named `data`:**

    ```bash
    python datadb.py data.csv
    ```

-   **Import a JSON file into a specific database and table:**

    ```bash
    python datadb.py data.json -d my_database.db -t my_table
    ```

-   **Append data from an Excel file to an existing table:**

    ```bash
    python datadb.py data.xlsx -e append
    ```

#### Exporting Data

-   **Export a table from a database to a CSV file:**

    ```bash
    python datadb.py output.csv -x -d my_database.db -t my_table
    ```
