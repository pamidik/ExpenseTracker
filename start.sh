#!/bin/bash

# Expense Tracker Startup Script for Mac
# Double-click this file to start the application

echo "======================================"
echo "💰 Starting Expense Tracker..."
echo "======================================"

# Get the directory where this script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Navigate to the directory
cd "$DIR"

# Check if Flask is installed
if ! python3 -c "import flask" 2>/dev/null; then
    echo "⚠️  Flask is not installed. Installing now..."
    pip3 install --user Flask openpyxl
fi

# Check if openpyxl is installed
if ! python3 -c "import openpyxl" 2>/dev/null; then
    echo "⚠️  openpyxl is not installed. Installing now..."
    pip3 install --user openpyxl
fi

# Start the application
python3 expense_tracker_app.py

# Keep terminal open on Mac
read -p "Press any key to close..."
