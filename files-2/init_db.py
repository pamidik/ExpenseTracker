import psycopg2
import os
import json

def get_db_connection():
    """Get database connection based on environment"""
    database_url = os.environ.get('DATABASE_URL')
    
    if database_url:
        # Production (Render) - uses DATABASE_URL
        conn = psycopg2.connect(database_url)
    else:
        # Local development
        conn = psycopg2.connect(
            host="localhost",
            database="expense_tracker",
            user="postgres",  # Change to your username if different
            password="your_password_here"  # Change to your PostgreSQL password
        )
    return conn

def init_database():
    """Create tables if they don't exist"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Create transactions table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id BIGINT PRIMARY KEY,
            date DATE NOT NULL,
            description TEXT NOT NULL,
            amount DECIMAL(10, 2) NOT NULL,
            category VARCHAR(100) NOT NULL,
            type VARCHAR(50) NOT NULL,
            status VARCHAR(50) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create categories table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create index for faster queries
    cur.execute('''
        CREATE INDEX IF NOT EXISTS idx_transactions_date 
        ON transactions(date DESC)
    ''')
    
    cur.execute('''
        CREATE INDEX IF NOT EXISTS idx_transactions_type 
        ON transactions(type)
    ''')
    
    conn.commit()
    cur.close()
    conn.close()
    
    print("✓ Database tables created successfully!")

def migrate_from_json():
    """Migrate existing data from JSON files to PostgreSQL"""
    
    # Check if JSON files exist
    if not os.path.exists('data/transactions.json'):
        print("No JSON files found to migrate")
        return
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Migrate categories
    try:
        with open('data/categories.json', 'r') as f:
            categories = json.load(f)
        
        for category in categories:
            cur.execute(
                'INSERT INTO categories (name) VALUES (%s) ON CONFLICT (name) DO NOTHING',
                (category,)
            )
        print(f"✓ Migrated {len(categories)} categories")
    except Exception as e:
        print(f"Categories migration: {e}")
    
    # Migrate transactions
    try:
        with open('data/transactions.json', 'r') as f:
            transactions = json.load(f)
        
        migrated = 0
        for t in transactions:
            try:
                cur.execute('''
                    INSERT INTO transactions (id, date, description, amount, category, type, status)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (id) DO NOTHING
                ''', (
                    t['id'],
                    t['date'],
                    t['description'],
                    t['amount'],
                    t['category'],
                    t['type'],
                    t.get('status', 'Done')
                ))
                migrated += 1
            except Exception as e:
                print(f"Error migrating transaction {t.get('id')}: {e}")
        
        conn.commit()
        print(f"✓ Migrated {migrated} transactions")
        
    except Exception as e:
        print(f"Transaction migration error: {e}")
    
    cur.close()
    conn.close()
    print("\n✓ Migration completed!")

if __name__ == '__main__':
    print("Initializing database...")
    init_database()
    
    print("\nMigrating data from JSON files...")
    migrate_from_json()
    
    print("\n✅ All done! Your PostgreSQL database is ready.")
