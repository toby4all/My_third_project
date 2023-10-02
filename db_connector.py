import pymysql

def add_user(user_id, username):
    schema_name = 'mydb'
    # Establishing a connection to the MySQL container within the Docker Compose network
    conn = pymysql.connect(host='mysql', port=3306, user='user', passwd='password', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from the database connection
    cursor = conn.cursor()

    # Inserting data into the table
    cursor.execute(f"INSERT into {schema_name}.users (user_id, name) VALUES ({user_id}, '{username}')")

    cursor.close()
    conn.close()

def get_user(user_id):
    schema_name = 'mydb'
    # Establishing a connection to the MySQL container within the Docker Compose network
    conn = pymysql.connect(host='mysql', port=3306, user='user', passwd='password', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from the database connection
    cursor = conn.cursor()

    # Select data from the table
    cursor.execute(f"SELECT name FROM {schema_name}.users WHERE user_id =({user_id}) ")
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

    cursor.close()
    conn.close()

def update_user(user_id, username):
    schema_name = 'mydb'
    # Establishing a connection to the MySQL container within the Docker Compose network
    conn = pymysql.connect(host='mysql', port=3306, user='user', passwd='password', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from the database connection
    cursor = conn.cursor()
    sql = f"UPDATE {schema_name}.users SET name = %s WHERE user_id = %s"
    val = (username, user_id)
    cursor.execute(sql, val)

    cursor.close()
    conn.close()

def delete_user(user_id):
    schema_name = 'mydb'
    # Establishing a connection to the MySQL container within the Docker Compose network
    conn = pymysql.connect(host='mysql', port=3306, user='user', passwd='password', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from the database connection
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {schema_name}.users WHERE user_id = '{user_id}'")

    cursor.close()
    conn.close()
