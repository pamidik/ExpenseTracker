# ⚡ QUICK START - 3 Steps

## Step 1: Download Everything
Download all files including the `templates` folder.

Your folder should look like this:
```
ExpenseTrackerApp/
├── expense_tracker_app.py
├── templates/
│   └── index.html
├── install.sh
├── start.sh
├── verify_setup.sh
├── requirements.txt
└── README.md
```

## Step 2: Verify Setup
```bash
cd /path/to/ExpenseTrackerApp
chmod +x verify_setup.sh
./verify_setup.sh
```

This will check if you have everything needed.

## Step 3: Install & Run
```bash
# Install dependencies
chmod +x install.sh
./install.sh

# Start the app
python3 expense_tracker_app.py
```

Open your browser to: **http://localhost:5001**

---

## 🎉 That's It!

### New Features:
- **⚙️ Settings Tab** - Change data storage location through the app
- **Custom Categories** - Add your own categories
- **Status Tracking** - Mark as Done or Scheduled
- **Excel Import** - Import your existing data
- **Excel/CSV Export** - Backup anytime

### Change Data Path:
1. Click **⚙️ Settings** tab
2. Enter new path (e.g., `~/Dropbox/ExpenseTracker`)
3. Click **Save**
4. Done! Setting persists forever

---

## 🆘 Troubleshooting:

**"Permission denied" when installing:**
```bash
pip3 install --user Flask openpyxl
```

**"Template not found":**
Make sure you have the `templates` folder with `index.html` inside it.

**Port 5000 blocked:**
The app auto-detects and uses port 5001. Check Terminal output for the actual port.

**Stop the app:**
Press `Ctrl+C` in Terminal

---

**No manual editing needed - everything works out of the box!** ✅
