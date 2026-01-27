import sqlite3

conn = sqlite3.connect('project.db')
cur = conn.cursor()

try:
    cur.execute("SELECT DISTINCT project_id FROM group_data")
    print("Existing project_ids:", cur.fetchall())
except sqlite3.OperationalError:
    print("No project_id column (or table doesn't exist)")
    
conn.close()
