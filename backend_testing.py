import requests
import pymysql

# request to post new data to the database with user_id '4'
res = requests.post('http://localhost:5000/users/4', json={"name": "Anabella"})
if res.status_code == 200:
    print(res.json())

# request to get data from the database with user_id '4'
response = requests.get('http://localhost:5000/users/4')
if response.ok:
    print(response.status_code)
    print(response.json())

# query the database to make sure the username is stored under id: '4'
schema_name = "mydb"

# Establishing a connection to the DB
conn = pymysql.connect(host='localhost', port=3306, user='user', passwd='password', db=schema_name)
# Getting a cursor from the Database
cursor = conn.cursor()

# Getting all data from the table "users"
cursor.execute(f"SELECT * FROM {schema_name}.users WHERE user_id = '4'")

# Iterating the table and printing all users
for row in cursor:
    print(row)

cursor.close()
conn.close()

# request to update user_name in the database to new data "George"
response = requests.put('http://localhost:5000/users/2', json={"name": "George"})
if response.ok:
    print(response.status_code)
    print(response.json())

# request to delete user_id "2"
response = requests.delete('http://localhost:5000/users/2')
if response.status_code == 200:
    print(response.json())
    print(response.status_code)
