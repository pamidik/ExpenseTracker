#!/bin/bash

# Installation Script for Mac Expense Tracker
# Run this first to install all dependencies

echo "======================================"
echo "📦 Installing Dependencies..."
echo "======================================"

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python version: $python_version"

# Install packages with --user flag to avoid permission issues
echo ""
echo "Installing Flask..."
pip3 install --user Flask

echo ""
echo "Installing openpyxl..."
pip3 install --user openpyxl

echo ""
echo "======================================"
echo "✅ Installation Complete!"
echo "======================================"
echo ""
echo "To start the application, run:"
echo "  python3 expense_tracker_app.py"
echo ""
echo "Or double-click: start.sh"
echo ""
