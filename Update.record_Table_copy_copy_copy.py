import os
import pymysql

# Get the username from the Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')
"""
One mething for making the update

try:
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'bob';")
        connection.commit()
"""

"""
try:
    # anoter method still a single line.
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
                       (23, 'bob'))
        connection.commit()
"""

try:
    # a method to update multiple rows.
    with connection.cursor() as cursor:
        rows = [(99, 'bob'),
                (88, 'jim'),
                (77, 'fred')]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;",
        #note the excutemany option.
                        rows)
        connection.commit()
finally:
    connection.close()
