import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='blog_db', charset='utf8mb4')
cursor = conn.cursor()

columns = [
    ('is_paid', 'ALTER TABLE projects ADD COLUMN is_paid TINYINT(1) DEFAULT 0'),
    ('is_featured', 'ALTER TABLE projects ADD COLUMN is_featured TINYINT(1) DEFAULT 0'),
    ('repost_url', 'ALTER TABLE projects ADD COLUMN repost_url VARCHAR(255) DEFAULT NULL'),
]

for col_name, alter_sql in columns:
    cursor.execute(f"SHOW COLUMNS FROM projects LIKE '{col_name}'")
    if not cursor.fetchone():
        cursor.execute(alter_sql)
        print(f'Added column: {col_name}')
    else:
        print(f'Column {col_name} already exists')

cursor.execute('SHOW TABLES LIKE "project_categories"')
if not cursor.fetchone():
    cursor.execute('''
        CREATE TABLE project_categories (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL UNIQUE,
            description TEXT,
            is_active TINYINT(1) DEFAULT 1,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP
        )
    ''')
    print('Created table: project_categories')
else:
    print('Table project_categories already exists')

conn.commit()
cursor.close()
conn.close()
print('Migration completed')