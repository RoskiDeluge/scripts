#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

PATH = "Downloads" # Enter the path to the folder
DIR = "subscribed_segment_*" # Enter the name of the directory to delete

def delete_dir():
    # Get downloads path using environment variable
    downloads_dir = Path.home() / PATH
    
    # Check if directory exists
    if downloads_dir.is_dir():
        # Find and delete all matching directories recursively
        for directory in downloads_dir.rglob(DIR):
            if directory.is_dir():  # Ensure it's a directory before deleting
                try:
                    shutil.rmtree(directory)
                    print(f"Deleted directory: {directory}")
                except Exception as e:
                    print(f"Failed to delete {directory}: {e}")
        print(f"All matching directories deleted from {downloads_dir} and subdirectories.")
    else:
        print("Downloads directory does not exist.")

if __name__ == "__main__":
    delete_dir()
