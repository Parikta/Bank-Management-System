from sqlconnection import get_sql_connection_second_instance


# Initialize database connection
mydb = get_sql_connection_second_instance()
cursor = mydb.cursor()

def db_query(query):
    """
    Execute a database query and return the results.
    """
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def create_customer_table():
    """
    Create the 'customers' table if it does not exist.
    """
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            username VARCHAR(20) NOT NULL,
            password VARCHAR(20) NOT NULL,
            name VARCHAR(20) NOT NULL,
            age INTEGER NOT NULL,
            city VARCHAR(20) NOT NULL,
            balance INTEGER NOT NULL,
            account_number INTEGER NOT NULL,
            status BOOLEAN NOT NULL
        )
    ''')
    mydb.commit()
    print("Customers table created successfully!")

if __name__ == "__main__":
    create_customer_table()


