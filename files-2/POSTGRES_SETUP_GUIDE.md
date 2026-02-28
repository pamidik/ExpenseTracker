# PostgreSQL Migration Guide

## Part 1: Local Setup

### Step 1: Install PostgreSQL

**Already done? Skip to Step 2.**

**Windows:**
- Download: https://www.postgresql.org/download/windows/
- Install with default settings
- Remember your password!

**Mac:**
```bash
brew install postgresql@15
brew services start postgresql@15
```

**Linux:**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
```

### Step 2: Create Database

**Option A - Using psql (Command Line):**
```bash
# Login to PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE expense_tracker;

# Exit
\q
```

**Option B - Using pgAdmin (GUI - Windows):**
1. Open pgAdmin 4
2. Right-click "PostgreSQL 15" → "Create" → "Database"
3. Name: `expense_tracker`
4. Click "Save"

### Step 3: Configure Database Password

**Edit `db_helper.py` line 23:**
```python
password=os.environ.get('DB_PASSWORD', 'YOUR_POSTGRES_PASSWORD_HERE')
```

Replace `YOUR_POSTGRES_PASSWORD_HERE` with your PostgreSQL password.

**Edit `init_db.py` line 15:**
```python
password="YOUR_POSTGRES_PASSWORD_HERE"
```

### Step 4: Install Python Dependencies

```bash
pip install psycopg2-binary
```

### Step 5: Initialize Database & Migrate Data

```bash
python init_db.py
```

This will:
- ✓ Create tables (transactions, categories)
- ✓ Migrate your existing JSON data to PostgreSQL
- ✓ Create indexes for performance

### Step 6: Test Locally

**Rename your app file:**
```bash
# Backup old version
mv expense_tracker_app.py expense_tracker_app_OLD.py

# Use new PostgreSQL version
mv expense_tracker_app_postgres.py expense_tracker_app.py
```

**Run the app:**
```bash
python expense_tracker_app.py
```

**Test at:** http://localhost:5000

---

## Part 2: Deploy to Render

### Step 1: Create PostgreSQL Database on Render

1. Log in to **Render.com**
2. Click **"New +"** → **"PostgreSQL"**
3. Settings:
   - Name: `expense-tracker-db`
   - Database: `expense_tracker`
   - User: `expense_tracker_user`
   - Region: Choose nearest to you
   - Plan: **Free**
4. Click **"Create Database"**
5. **Wait 2-3 minutes** for it to be created
6. **Copy** the **"Internal Database URL"** - looks like:
   ```
   postgres://expense_tracker_user:xxxxx@dpg-xxxxx/expense_tracker
   ```

### Step 2: Create Web Service on Render

1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository: `pamidik/ExpenseTracker`
3. Settings:
   - **Name:** `expense-tracker`
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt && python init_db.py`
   - **Start Command:** `gunicorn expense_tracker_app:app`
   - **Instance Type:** Free

### Step 3: Add Environment Variable

In the Web Service settings:
1. Scroll to **"Environment Variables"**
2. Click **"Add Environment Variable"**
3. Add:
   - **Key:** `DATABASE_URL`
   - **Value:** Paste the Internal Database URL from Step 1
4. Click **"Save Changes"**

### Step 4: Deploy

1. Click **"Manual Deploy"** → **"Deploy latest commit"**
2. Wait 3-5 minutes for build and deployment
3. Your app will be live at: `https://expense-tracker-XXXX.onrender.com`

---

## Part 3: Verify Everything Works

### Local Testing:
```bash
# Check tables were created
psql -U postgres -d expense_tracker -c "\dt"

# Check data was migrated
psql -U postgres -d expense_tracker -c "SELECT COUNT(*) FROM transactions;"
```

### Production Testing:
1. Visit your Render URL
2. Add a test transaction
3. Refresh the page - transaction should persist!
4. Check Render logs for any errors

---

## Troubleshooting

### Error: "password authentication failed"
**Fix:** Update password in `db_helper.py` and `init_db.py`

### Error: "database does not exist"
**Fix:** Run `CREATE DATABASE expense_tracker;` in psql

### Error: "ModuleNotFoundError: psycopg2"
**Fix:** Run `pip install psycopg2-binary`

### Render deploy fails:
**Check:** Render logs for specific error
**Common:** DATABASE_URL environment variable not set

### Data not persisting on Render:
**Check:** DATABASE_URL is set correctly
**Check:** init_db.py ran successfully (check build logs)

---

## File Checklist

Make sure these files are in your project:

- ✅ `expense_tracker_app.py` (new PostgreSQL version)
- ✅ `db_helper.py` (database functions)
- ✅ `init_db.py` (database initialization)
- ✅ `requirements.txt` (with psycopg2-binary)
- ✅ `templates/index.html` (unchanged)

---

## Benefits of PostgreSQL

✅ **Persistent Storage** - Data survives app restarts
✅ **Better Performance** - Indexed queries, faster than JSON
✅ **Concurrent Access** - Multiple users can access safely
✅ **Backup & Restore** - Built-in database tools
✅ **Scalability** - Can handle millions of transactions
✅ **Free on Render** - 90-day expiry, but can be extended

---

## Next Steps

1. Test locally first
2. Push to GitHub
3. Deploy to Render
4. Add custom domain (optional)
5. Enjoy your persistent expense tracker! 🎉
