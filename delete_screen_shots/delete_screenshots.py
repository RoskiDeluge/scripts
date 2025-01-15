#!/usr/bin/env python3
import os
import glob
from pathlib import Path

def delete_screenshots():
    # Get desktop path using environment variable
    desktop_dir = str(Path.home() / "Desktop")
    
    # Check if directory exists
    if os.path.isdir(desktop_dir):
        # Find and delete all screenshots
        screenshot_pattern = os.path.join(desktop_dir, "ss_*.png")
        for screenshot in glob.glob(screenshot_pattern):
            os.remove(screenshot)
        print(f"All screenshots deleted from {desktop_dir}")
    else:
        print("Desktop directory does not exist.")

if __name__ == "__main__":
    delete_screenshots()
