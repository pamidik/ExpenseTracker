# 🚀 Expense Tracker - Complete Deployment Package

## ✅ What's Included:

This is a **COMPLETE, READY-TO-USE** package. No manual editing required!

### Files:
```
ExpenseTrackerApp/
├── expense_tracker_app.py    ✅ Complete with Settings API
├── templates/
│   └── index.html            ✅ Complete with all tabs including Settings
├── install.sh                ✅ Automated installation script
├── start.sh                  ✅ Automated startup script
├── requirements.txt          ✅ All dependencies listed
└── README.md                 ✅ This file
```

---

## 🎯 Quick Start (3 Steps):

### Step 1: Download All Files
Download the entire package and place all files in a folder (e.g., `ExpenseTrackerApp`)

**IMPORTANT:** Make sure you have:
- `expense_tracker_app.py`
- `templates/` folder with `index.html` inside it
- All .sh scripts

### Step 2: Install Dependencies
Open Terminal, navigate to your folder, and run:

```bash
cd /path/to/ExpenseTrackerApp
chmod +x install.sh
./install.sh
```

Or manually:
```bash
pip3 install --user Flask openpyxl
```

### Step 3: Run the App
```bash
python3 expense_tracker_app.py
```

Then open your browser to the URL shown (usually `http://localhost:5001`)

---

## ✨ What's New - Settings Feature:

### Change Data Storage Location Through the App!

1. **Click the ⚙️ Settings tab**
2. **Enter your preferred path** (e.g., `~/Dropbox/ExpenseTracker`)
3. **Click "Save Settings"**
4. **Done!** The setting persists forever

### Example Storage Locations:
```bash
~/Documents/ExpenseTracker          # Default local storage
~/Dropbox/Finance/ExpenseTracker    # Dropbox (cloud backup)
~/Google Drive/ExpenseTracker       # Google Drive (sync)
/Volumes/MyUSB/ExpenseTracker       # External drive
```

### How It Works:
- Config saved in: `~/.expense_tracker_config.json`
- Persists across app restarts
- Survives app updates
- Can be changed anytime through Settings tab

---

## 📋 Features:

✅ **Dashboard** - Real-time overview of income, expenses, balance  
✅ **Transactions** - Add, view, filter, delete with status tracking (Done/Scheduled)  
✅ **Custom Categories** - Create your own categories  
✅ **Budgets** - Set monthly limits and track spending  
✅ **Analytics** - Visual charts and insights  
✅ **Excel Import/Export** - Import existing data, export for backup  
✅ **Settings** - **NEW!** Change data storage location through the app  

---

## 🔧 Troubleshooting:

### "Permission Denied" when installing
```bash
pip3 install --user Flask openpyxl
```

### "Port 5000 in use" or HTTP 403
The app automatically tries ports 5000-5010. Check Terminal output for the actual port.

### "Template Not Found"
Make sure the `templates` folder exists with `index.html` inside it.

### Can't connect to localhost
Make sure the app is running in Terminal. You should see:
```
🌐 Access the app at: http://localhost:5001
```

---

## 📂 Data Storage:

### Default Location:
```
~/Documents/ExpenseTracker/
├── transactions.json
├── budgets.json
└── categories.json
```

### Config File:
```
~/.expense_tracker_config.json
```

This config file stores your settings (like data path) and persists across restarts.

---

## 💡 Pro Tips:

1. **Cloud Sync:** Set data path to Dropbox/Google Drive for automatic backups
2. **Multiple Devices:** Use cloud storage to access data from different computers
3. **Backup:** Use the Export Excel/CSV feature regularly
4. **Reset:** Delete `~/.expense_tracker_config.json` to reset to defaults

---

## 🆘 Need Help?

### Common Issues:

**Q: How do I stop the app?**  
A: Press `Ctrl+C` in the Terminal window where it's running

**Q: Can I change the data path after I've added transactions?**  
A: Yes! But the old data won't move automatically. You can:
1. Change to new path in Settings
2. Manually copy the JSON files from old to new location
3. Or use the new location for future data

**Q: Where is my data actually stored?**  
A: Check the Settings tab - it shows your current storage location

**Q: The app won't start**  
A: Make sure:
- You're in the correct folder
- The `templates` folder exists with `index.html` inside
- Dependencies are installed (`pip3 install --user Flask openpyxl`)

---

## 🎉 You're All Set!

Your expense tracker is now fully deployed with:
- ✅ Configurable storage location
- ✅ Custom categories
- ✅ Status tracking
- ✅ Excel import/export
- ✅ All features ready to use

**No manual editing required - everything works out of the box!**

---

**Built with:** Python Flask, Chart.js, and ❤️

**Version:** 2.0 (With Settings Feature)
