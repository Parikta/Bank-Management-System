import mysql.connector

cnx = None  # Initialize the global variable

def get_sql_connection_second_instance():
    global cnx
    print("Opening connection to the second MySQL instance")

    if cnx is None:
        cnx = mysql.connector.connect(
            user='root', 
            password='Bsb@9108', 
            database='bankmanagementsystem',
            host='127.0.0.1',  # Local instance
            port=3306         # Port of the second instance
        )
    
    return cnx

