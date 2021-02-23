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
# delete a single row
try:
    with connection.cursor() as cursor:
        rows = cursor.execute("DELETE FROM Friends WHERE name = 'bob';")
        connection.commit()
"""

"""
# another method to delete on line. 
try:
    with connection.cursor() as cursor:
        rows = cursor.execute("DELETE FROM Friends WHERE name = %s;", 'jim')
        connection.commit()
"""

"""
# delete multiple lines.
try:
    with connection.cursor() as cursor:
        rows = cursor.executemany("DELETE FROM Friends WHERE name = %s;", ['bob', 'jim', 'fred'])
        connection.commit()
"""

try:
    #
    with connection.cursor() as cursor:
        list_of_names = ['fred', 'jim', 'bob']
        # Prepare a string with same number of placeholders as in list_of_names
        format_strings = ','.join(['%s'] * len(list_of_names))
        cursor.execute(
            "DELETE FROM Friends WHERE name in ({});".format(format_strings), 
            # dynamicaly deletes based on the number of items in the list (list_of_names)
            list_of_names)

        connection.commit()

finally:
    connection.close()
