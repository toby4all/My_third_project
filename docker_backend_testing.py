import requests
import pymysql

# request to post new data to database with usr_name 'John'
res = requests.post('http://127.0.0.1:5000/users/5', json={"name": "Micheal"})
if res.status_code == 200:
    print(res.json())

# request to get data from database with usr_id '5'
response = requests.get('http://127.0.0.1:5000/users/5')
if response.ok:
    print(response.status_code)
    print(response.json())

# query database to make sure username is stored under id:'5'
#
schema_name = "mydb"

# Establishing a connection to DB
conn = pymysql.connect(host='127.0.0.1', port=3306, user='user', passwd='password', db=schema_name)
# Getting a cursor from Database
cursor = conn.cursor()

# Getting all data from table “users”
cursor.execute(f"SELECT * FROM {schema_name}.users WHERE user_id ='5'")

# Iterating table and printing all users
for row in cursor:
    print(row)

cursor.close()
conn.close()

# request to update user_name in database to new data "George"
response = requests.put('http://127.0.0.1:5000/users/2', json={"name": "George"})
if response.ok:
    print(response.status_code)
    print(response.json())

# request to delete user_id "2"
response = requests.delete('http://127.0.0.1:5000/users/2')
if response.status_code == 2:
    print(response.json())
    print(response.status_code)