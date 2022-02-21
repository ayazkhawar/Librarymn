import mysql.connector
from mysql.connector import Error
conn = mysql.connector.connect(host='localhost',
                                         database='librarymn',
                                         user='root',
                                         password='Admin_123_4')