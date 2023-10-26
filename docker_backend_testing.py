import requests
import pymysql
import time

# Wait for services to start
time.sleep(10)

# request to post new data to the database with user_id '5'
res = requests.post('http://devops-rest:5000/users/5', json={"name": "Micheal"})
if res.status_code == 200:
    print(res.json())

# request to get data from the database with user_id '5'
response = requests.get('http://devops-rest:5000/users/5')
if response.ok:
    print(response.status_code)
    print(response.json())

# query the database to make sure username is stored under id: '5'
schema_name = "mydb"

# Establishing a connection to the database
conn = pymysql.connect(host='db', port=3306, user='user', passwd='password', db=schema_name)
# Getting a cursor from the database
cursor = conn.cursor()

# Getting all data from table "users"
cursor.execute(f"SELECT * FROM {schema_name}.users WHERE user_id = '5'")

# Iterating the table and printing all users
for row in cursor:
    print(row)

cursor.close()
conn.close()

# request to update user_name in the database to new data "George"
response = requests.put('http://devops-rest:5000/users/2', json={"name": "George"})
if response.ok:
    print(response.status_code)
    print(response.json())

# request to delete user_id "2"
response = requests.delete('http://devops-rest:5000/users/2')
if response.status_code == 200:
    print(response.json())
    print(response.status_code)
