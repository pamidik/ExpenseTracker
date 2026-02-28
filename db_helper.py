"""
Database helper functions for PostgreSQL
"""
import psycopg2
import psycopg2.extras
import os
from decimal import Decimal

def get_db_connection():
    """Get database connection based on environment"""
    database_url = os.environ.get('DATABASE_URL')
    
    if database_url:
        # Production (Render) - DATABASE_URL is provided
        # Render uses postgres:// but psycopg2 needs postgresql://
        if database_url.startswith('postgres://'):
            database_url = database_url.replace('postgres://', 'postgresql://', 1)
        conn = psycopg2.connect(database_url)
    else:
        # Local development
        conn = psycopg2.connect(
            host=os.environ.get('DB_HOST', 'localhost'),
            database=os.environ.get('DB_NAME', 'expense_tracker'),
            user=os.environ.get('DB_USER', 'postgres'),
            password=os.environ.get('DB_PASSWORD', 'Starts123')  # CHANGE THIS!
        )
    return conn

def load_transactions():
    """Load all transactions from database"""
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    
    cur.execute('''
        SELECT id, date::text, description, amount, category, type, status
        FROM transactions
        ORDER BY date DESC
    ''')
    
    transactions = cur.fetchall()
    cur.close()
    conn.close()
    
    # Convert to list of dicts and handle Decimal types
    result = []
    for t in transactions:
        result.append({
            'id': t['id'],
            'date': t['date'],
            'description': t['description'],
            'amount': float(t['amount']),
            'category': t['category'],
            'type': t['type'],
            'status': t['status']
        })
    
    return result

def load_categories():
    """Load all categories from database"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute('SELECT name FROM categories ORDER BY name')
    categories = [row[0] for row in cur.fetchall()]
    
    cur.close()
    conn.close()
    
    return categories

def add_transaction(transaction):
    """Add a new transaction to database"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute('''
        INSERT INTO transactions (id, date, description, amount, category, type, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING id
    ''', (
        transaction['id'],
        transaction['date'],
        transaction['description'],
        transaction['amount'],
        transaction['category'],
        transaction['type'],
        transaction.get('status', 'Done')
    ))
    
    transaction_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    
    return transaction_id

def update_transaction(transaction_id, transaction):
    """Update an existing transaction"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute('''
        UPDATE transactions
        SET date = %s,
            description = %s,
            amount = %s,
            category = %s,
            type = %s,
            status = %s
        WHERE id = %s
    ''', (
        transaction['date'],
        transaction['description'],
        transaction['amount'],
        transaction['category'],
        transaction['type'],
        transaction.get('status', 'Done'),
        transaction_id
    ))
    
    conn.commit()
    cur.close()
    conn.close()

def delete_transaction(transaction_id):
    """Delete a transaction"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute('DELETE FROM transactions WHERE id = %s', (transaction_id,))
    
    conn.commit()
    cur.close()
    conn.close()

def bulk_update_transactions(transaction_ids, field, value):
    """Bulk update multiple transactions"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Validate field to prevent SQL injection
    allowed_fields = ['category', 'type', 'status']
    if field not in allowed_fields:
        raise ValueError(f"Invalid field: {field}")
    
    # Use parameterized query
    query = f'UPDATE transactions SET {field} = %s WHERE id = ANY(%s)'
    cur.execute(query, (value, transaction_ids))
    
    conn.commit()
    cur.close()
    conn.close()

def add_category(category_name):
    """Add a new category"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        cur.execute(
            'INSERT INTO categories (name) VALUES (%s) ON CONFLICT (name) DO NOTHING',
            (category_name,)
        )
        conn.commit()
        success = True
    except Exception as e:
        print(f"Error adding category: {e}")
        success = False
    
    cur.close()
    conn.close()
    
    return success
