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