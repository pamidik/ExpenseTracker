#!/bin/bash

# Complete Deployment Verification Script

echo "======================================"
echo "🔍 Verifying Expense Tracker Setup"
echo "======================================"
echo ""

all_good=true
missing_files=""

# Check Python file
if [ -f "expense_tracker_app.py" ]; then
    echo "✅ expense_tracker_app.py found"
    # Check if it has the settings feature
    if grep -q "def update_config" expense_tracker_app.py; then
        echo "   ✅ Settings feature included"
    else
        echo "   ⚠️  Old version detected (no settings feature)"
        all_good=false
    fi
else
    echo "❌ expense_tracker_app.py NOT FOUND"
    missing_files="$missing_files\n  - expense_tracker_app.py"
    all_good=false
fi

# Check templates folder
if [ -d "templates" ]; then
    echo "✅ templates/ folder found"
    
    # Check for index.html
    if [ -f "templates/index.html" ]; then
        echo "   ✅ templates/index.html found"
        
        # Check if it has the settings tab
        if grep -q "Settings Tab" templates/index.html; then
            echo "   ✅ Settings tab included"
        else
            echo "   ⚠️  Old version detected (no settings tab)"
            all_good=false
        fi
    else
        echo "   ❌ templates/index.html NOT FOUND"
        missing_files="$missing_files\n  - templates/index.html"
        all_good=false
    fi
else
    echo "❌ templates/ folder NOT FOUND"
    missing_files="$missing_files\n  - templates/ folder"
    all_good=false
fi

# Check requirements.txt
if [ -f "requirements.txt" ]; then
    echo "✅ requirements.txt found"
else
    echo "⚠️  requirements.txt not found (optional)"
fi

# Check install script
if [ -f "install.sh" ]; then
    echo "✅ install.sh found"
else
    echo "⚠️  install.sh not found (optional)"
fi

# Check start script
if [ -f "start.sh" ]; then
    echo "✅ start.sh found"
else
    echo "⚠️  start.sh not found (optional)"
fi

# Check README
if [ -f "README.md" ]; then
    echo "✅ README.md found"
else
    echo "⚠️  README.md not found (optional)"
fi

echo ""
echo "======================================"

if [ "$all_good" = true ]; then
    echo "✅ All required files present!"
    echo ""
    echo "Your setup is complete and ready to use."
    echo ""
    echo "To start the app, run:"
    echo "  python3 expense_tracker_app.py"
    echo ""
    echo "Features included:"
    echo "  ✅ Settings tab (configurable data path)"
    echo "  ✅ Custom categories"
    echo "  ✅ Status tracking (Done/Scheduled)"
    echo "  ✅ Excel import/export"
    echo "  ✅ Budget management"
    echo "  ✅ Analytics & charts"
else
    echo "❌ Setup incomplete!"
    echo ""
    echo "Missing or outdated files:"
    echo -e "$missing_files"
    echo ""
    echo "Please download all required files:"
    echo "  1. expense_tracker_app.py (with Settings feature)"
    echo "  2. templates/ folder with index.html inside"
    echo ""
    echo "Make sure you're downloading the COMPLETE package"
    echo "with all features integrated."
fi

echo "======================================"
echo ""

# Check Python
echo "Checking Python installation..."
if command -v python3 &> /dev/null; then
    python_version=$(python3 --version 2>&1)
    echo "✅ Python installed: $python_version"
else
    echo "❌ Python 3 not found"
    echo "   Install from: https://www.python.org/downloads/"
fi

# Check Flask
echo ""
echo "Checking dependencies..."
if python3 -c "import flask" 2>/dev/null; then
    echo "✅ Flask installed"
else
    echo "❌ Flask not installed"
    echo "   Run: pip3 install --user Flask openpyxl"
fi

if python3 -c "import openpyxl" 2>/dev/null; then
    echo "✅ openpyxl installed"
else
    echo "❌ openpyxl not installed"
    echo "   Run: pip3 install --user Flask openpyxl"
fi

echo ""
echo "======================================"
