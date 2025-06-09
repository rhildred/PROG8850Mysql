# execute_schema_changes.py
# pyright: ignore[reportMissingImports]

import mysql.connector

config = {
    'host': 'SumanKumari',
    'user': 'suman',
    'password': 'suman123',
    'database': 'companydb'
}

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    with open('schema_changes.sql', 'r') as f:
        sql_commands = f.read().split(';')

        for command in sql_commands:
            command = command.strip()
            if command:
                cursor.execute(command)

    conn.commit()
    print("Schema changes applied successfully.")

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
