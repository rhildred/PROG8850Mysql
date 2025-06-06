import mysql.connector

# Database connection details
config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'Secret5555',  
    'database': 'test'         
}

def execute_sql_script(filename, config):
    # Connect to MySQL
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    with open(filename, 'r') as f:
        sql_script = f.read()
    # Split script into individual statements
    for statement in sql_script.split(';'):
        stmt = statement.strip()
        if stmt:
            try:
                cursor.execute(stmt)
                print(f"Executed: {stmt[:60]}...")
            except mysql.connector.Error as err:
                # Ignore duplicate column error for 'budget'
                if err.errno == 1060 and "budget" in stmt:
                    print("Column 'budget' already exists, skipping.")
                else:
                    print(f"Error executing: {stmt[:60]}...\n{err}")
    conn.commit()
    cursor.close()
    conn.close()
    print("All statements executed and committed.")

if __name__ == "__main__":
    execute_sql_script('schema_changes.sql', config)
    execute_sql_script('adddept_table.sql', config)
    