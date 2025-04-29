# datadb.py: Utility for importing/exporting data between files and SQLite DB
import sqlite3  # SQLite database module
import pandas as pd  # Data analysis library
import os  # OS utilities for file handling
import argparse  # Command-line argument parsing


def get_file_extension(file_path):
    """Extract file extension from file path (e.g., .csv, .json, .xlsx)."""
    _, extension = os.path.splitext(file_path)
    return extension.lower()


def read_file_to_dataframe(file_path):
    """Read different file formats into a pandas DataFrame.
    Supports: .csv, .json, .xlsx, .xls
    """
    extension = get_file_extension(file_path)

    if extension == '.csv':
        return pd.read_csv(file_path)  # Read CSV file
    elif extension == '.json':
        return pd.read_json(file_path)  # Read JSON file
    elif extension in ['.xlsx', '.xls']:
        return pd.read_excel(file_path)  # Read Excel file
    else:
        raise ValueError(
            f"Unsupported file format: {extension}. Supported formats are .csv, .json, .xlsx, and .xls")


def export_table_to_file(db_name, table_name, output_file):
    """Export a table from the SQLite database to a file (CSV, JSON, Excel)."""
    conn = sqlite3.connect(db_name)

    # Check if table exists in the database
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    if not cursor.fetchone():
        raise ValueError(
            f"Table '{table_name}' does not exist in database '{db_name}'")

    # Read the table into a DataFrame
    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)

    # Determine the output format based on file extension
    extension = get_file_extension(output_file)

    if extension == '.csv':
        df.to_csv(output_file, index=False)
    elif extension == '.json':
        df.to_json(output_file, orient='records')
    elif extension in ['.xlsx', '.xls']:
        df.to_excel(output_file, index=False)
    else:
        raise ValueError(
            f"Unsupported output format: {extension}. Supported formats are .csv, .json, .xlsx, and .xls")

    conn.close()
    return len(df)


def main():
    # Set up argument parser with description, examples, and formatted help
    parser = argparse.ArgumentParser(
        description='Convert between data files and SQLite database.',
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=(
            'Examples:\n'
            '  # Import data.csv into default main.db, table name data\n'
            '  python datadb.py data.csv\n\n'
            '  # Import data.json into my.db, table=mytable\n'
            '  python datadb.py data.json -d my.db -t mytable\n\n'
            '  # Append Excel data to existing table\n'
            '  python datadb.py data.xlsx -e append\n\n'
            '  # Export table from DB to CSV\n'
            '  python datadb.py output.csv -x -d my.db -t mytable\n'
        )
    )
    parser.add_argument('file_path', help='Path to the input/output file')
    parser.add_argument('-t', '--t', dest='table_name',
                        help='Name for the SQL table', default=None)
    parser.add_argument('-d', '--d', dest='db_name',
                        help='Name for the SQLite database', default='main.db')
    parser.add_argument('-e', '--e', dest='if_exists', choices=['replace', 'append', 'fail'],
                        help='Action if table exists (replace/append/fail)', default='replace')
    parser.add_argument('-x', '--x', dest='export', action='store_true',
                        help='Export mode: export table to file instead of importing')

    args = parser.parse_args()

    # If table name not provided, use the file name without extension
    if args.table_name is None:
        args.table_name = os.path.splitext(os.path.basename(args.file_path))[0]

    try:
        if args.export:
            # Export mode: table to file
            print(
                f"Exporting table '{args.table_name}' from database '{args.db_name}' to '{args.file_path}'...")
            rows = export_table_to_file(
                args.db_name, args.table_name, args.file_path)
            print(f"Successfully exported {rows} rows to {args.file_path}")
        else:
            # Import mode: file to table
            print(f"Reading {args.file_path}...")
            df = read_file_to_dataframe(args.file_path)

            # Connect to SQLite database
            print(f"Connecting to {args.db_name}...")
            conn = sqlite3.connect(args.db_name)

            # Write the data to a SQLite table
            print(
                f"Writing data to table '{args.table_name}' with '{args.if_exists}' mode...")
            df.to_sql(args.table_name, conn,
                      if_exists=args.if_exists, index=False)

            print(
                f"Successfully imported {len(df)} rows into {args.table_name}")
            conn.close()
            print("Database connection closed.")

    except Exception as e:
        print(f"Error: {e}")
        if 'conn' in locals():
            conn.close()


if __name__ == "__main__":
    main()
