#!/bin/zsh

# Define the Desktop directory
DESKTOP_DIR="$HOME/Desktop"

# Check if the directory exists
if [[ -d "$DESKTOP_DIR" ]]; then
    # Find and delete all screenshots in the Desktop directory
    find "$DESKTOP_DIR" -type f -name "Screenshot *.png" -delete
    echo "All screenshots deleted from $DESKTOP_DIR"
else
    echo "Documents directory does not exist."
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
fi
