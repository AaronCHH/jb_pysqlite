# Ch13 Pyton 內嵌式資料庫 SQLite

{cite}`Python程式設計實用經典_2016`

# %load sqlite_creatDB_Table.py
# filename:sqlite_CreateDB_Table.py
# function: Python program using Sqlite
# Step1: Create user DB name using Sqlite3.connect("DB name)
# step2: Create Table using CREATE TABLE Table_name
# step3: insert Data value using INSERT INTO invest VALUES

import sqlite3
conndb = sqlite3.connect('chap13_DB.db')
curr = conndb.cursor()

# Create table using CREATE TABLE Table_name
curr.execute(
  "CREATE TABLE invest(date text, trans text, Company text, qty int, price real)")

# Insert a row of data
curr.execute("INSERT INTO invest VALUES ('2016-03-01','BUY','Mediatek',10,120)")

# commit the changes, it means save the data
conndb.commit()

curr.execute('select * from invest')
data_fromDB = curr.fetchall()
print(data_fromDB)

# inserts many records at a time
buy_sell = [('2016-03-28', 'BUY', 'Mediatek', 10, 123.00),
            ('2016-05-02', 'BUY', 'TSMC', 20, 120.00),
            ('2006-05-12', 'SELL', 'Mediatek', 10, 125.00),
            ('2006-05-13', 'SELL', 'TSMC', 20, 125.00),
            ]
curr.executemany('INSERT INTO invest VALUES (?,?,?,?,?)', buy_sell)
conndb.commit()

# fetch the data from DB's table
curr.execute('select * from invest')
data = curr.fetchall()
print(data)

# close the connection .
curr.close()
conndb.close()

# %load sqlite_retrive.py
# filename:Sqlite_retrive.py
# function: retrive row data
# The original table is created by using the following statement
#curr.execute("CREATE TABLE invest(date text, trans text, Company text, qty int, price real)")

import sqlite3 as DB
import sys


connDB = DB.connect('chap13_db.db')
with connDB:
  cur = connDB.cursor()
  cur.execute("SELECT * FROM invest")

  rows = cur.fetchall()
  print("The Data from invest table are as follows:\n")
  print(" date          trans  Company    qty  price")
  print("===========================================")
  for row in rows:
    print(row)

  cur.execute("SELECT * FROM invest WHERE Company= 'TSMC'  AND trans= 'BUY' ")

  BUY_amount = 0
  amount = 0
  BUY_records = cur.fetchall()
  print("\nThe Data from invest for TSMC BUY are as follows:\n")
  for row in BUY_records:
    print(row)
#   cur.execute("SELECT sum(qty*price) AS 'Total monthly salary' FROM invest")
    amount = row[3]*row[4]
    print("row amount=", amount)
    BUY_amount += amount
  print("BUY_amount=", BUY_amount)

  cur.execute("SELECT * FROM invest WHERE Company= 'TSMC'  AND trans= 'SELL' ")

  SELL_amount = 0
  amount = 0
  SELL_records = cur.fetchall()
  print("\nThe Data from invest for TSMC SELL  are as follows:\n")
  for row in SELL_records:
    print(row)
    amount = row[3]*row[4]
    print("row amount=", amount)
    SELL_amount += amount
  print("SELL_amount=", SELL_amount)

  print(" The invest result=", (SELL_amount-BUY_amount)*1000, " NTD")

# close the connection .
cur.close()
connDB.close()

# %load sqlite_create_insert_only.py
# filename:sqlite_Create_insert_only.py
# function: create Database name and Table and insrt values

import sqlite3 as DBlite

conn = DBlite.connect("D:/BOOK/CHAP14/CHAP13_TEST.DB")
cursor = conn.cursor()

cursor.execute("""drop table if exists books""")

# create a table
# cursor.execute("""CREATE TABLE albums
#                  (title text, artist text, release_date text,
#                   publisher text, media_type text)
#               """)
cursor.execute("""CREATE TABLE books
                  (book_id  text, title text, author text, release_date text, 
                   book_company text, category_type text) 
               """)
# insert some data
cursor.execute(
  "INSERT INTO books VALUES ('0-13-020272-x','Unix Network programming', 'Steven ', '10/12/2000', 'Osliiy', 'Network')")

# commit, means to save data to database
conn.commit()

# insert multiple records, using the more secure "?" method
# cursorname.execitemany
BOOKS_data = [('1-878739-02-6', 'c++ primer', 'Stephen', '12/8/2000', 'Waite Group', 'Language'),
              ('0-13-2017-1', 'The design of the UNix OS', 'J.Bach', '3/2/2002', 'Prentice', 'OS')]
cursor.executemany("INSERT INTO books VALUES (?,?,?,?,?,?)", BOOKS_data)
conn.commit()

print("\nList all the records in the table after INSERT :\n")
for row_record in cursor.execute("SELECT rowid, * FROM books ORDER BY category_type"):
  print(row_record)

embedded_sql_alter = """
ALTER TABLE books ADD price int
"""
cursor.execute(embedded_sql_alter)
conn.commit()

print("\nList all the records in the table after ALTER :\n")
for row_record in cursor.execute("SELECT rowid, * FROM books ORDER BY category_type"):
  print(row_record)

embedded_sql = """
UPDATE books SET author = 'Maurice J.Bach' WHERE author = 'J.Bach'
"""
cursor.execute(embedded_sql)
conn.commit()
print("\nList all the records in the table after UPDATE :\n")
for row_record in cursor.execute("SELECT rowid, * FROM books ORDER BY category_type"):
  print(row_record)


sql = """ DELETE FROM books WHERE author = 'Stephen'
"""
cursor.execute(sql)
conn.commit()
print("\nList all the records in the table after DELETE FROM TABLE:\n")
for row_record in cursor.execute("SELECT rowid, * FROM books ORDER BY category_type"):
  print(row_record)

# %load sqlite_datatype.py
# filename:sqlite_Datatype.py
# function: show the data type

import sqlite3
sql_create_cusomer_table = """
CREATE TABLE IF NOT EXISTS customer (
  Customer_id  INT  PRIMARY KEY  DEFAULT 1101,
  Cust_Name VARCHAR(10) NOT NULL DEFAULT "APPLE",
  Credit int  NOT NULL DEFAULT 10000,
  Phone   VARCHAR(10) NULL
);
"""

db_file = "D:/BOOK/CHAP14/CHAP13_TEST.DB"

try:
  conn = sqlite3.connect(db_file)
  print(conn)

except Error as err:
  print(err)
else:
  print("OK")

conn.execute(sql_create_cusomer_table)

customer_data = [(1102, "APPLE", 10000, "212-3312456"),
                 (1101, "IBM", 20000, ""),
                 (1103, "Google", 30000, "716-3222222")]
cursor = conn.cursor()
cursor.executemany("INSERT INTO customer VALUES (?,?,?,?)", customer_data)
print("\nList all the records in the table after INSERT :\n")
for row_record in cursor.execute("SELECT rowid, * FROM customer ORDER BY Customer_id"):
  print(row_record)

# %load sqlite_DML.py
# filename:sqlite_DML.py
# function: select Row data

import sqlite3 as DBlite

conn = DBlite.connect("D:/BOOK/CHAP14/CHAP13_TEST.DB")
cursor = conn.cursor()
cursor.execute("""DROP TABLE if exists books""")

cursor.execute("""CREATE TABLE books
                  (book_id  text, title text, author text, release_date text, 
                   book_company text, category_type text) 
               """)
# insert data
cursor.execute(
  "INSERT INTO books VALUES ('0-13-020272-x','Unix Network programming', 'Steven ', '10/12/2000', 'Osliiy', 'Network')")
# save data to database
conn.commit()

# insert multiple records(row) using cursorname.execitemany
BOOKS_data = [('1-878739-02-6', 'c++ primer', 'Stephen', '12/8/2000', 'Waite Group', 'Language'),
              ('0-13-2017-1', 'The design of the UNix OS',
               'J.Bach', '3/2/2002', 'Prentice', 'OS'),
              ('0-13-2016-1', 'The Python programming', 'S.HSU', '3/2/2016', 'songkung', 'language')]
cursor.executemany("INSERT INTO books VALUES (?,?,?,?,?,?)", BOOKS_data)
conn.commit()

print("\nList all the records in the table after INSERT :\n")
for row_record in cursor.execute("SELECT rowid, * FROM books ORDER BY category_type"):
  print(row_record)

print("\nResults from a LIKE query:\n")
select_sql = """
SELECT * FROM books 
WHERE title LIKE '%python%' """
cursor.execute(select_sql)
print(cursor.fetchall())

print("\nDELETE author is J.Bach:\n")
delete_sql = """DELETE FROM  books where author="J.Bach"
"""
cursor.execute(delete_sql)
conn.commit()
for row_record in cursor.execute("SELECT rowid, * FROM books ORDER BY category_type"):
  print(row_record)

# %load primary_key.py
#filename: primary_key.py
# function: create table using primay key and select two table such as orders and customers

import sqlite3


# create a Database
def db_connect(db):

  try:
    conn = sqlite3.connect(db)
    print("conn=", conn)
    return conn
  except Error as err:
    print(err)
    return None
  else:
    print("connection DB is ok")


def create_table(conn, create_table):
  try:
    c = conn.cursor()
    c.execute(create_table)
  except Error as err:
    print(err)
    return NONE
  else:
    print("Create TABLE OK")
    return c
  finally:
    print("Finally")


def main():
  dbfile = "D:/BOOK/CHAP14/CHAP13_TEST.DB"

  sql_create_customers_table = """ CREATE TABLE IF NOT EXISTS customers (
                                        id         integer PRIMARY KEY,
                                        name       text NOT NULL,
                                        begin_date text,
                                        credit     integer NOT NULL
                                    ); """

  sql_create_orders_table = """CREATE TABLE IF NOT EXISTS orders (
                                    id            integer PRIMARY KEY,
                                    name          text NOT NULL,
                                    quantity      integer,
                                    product       integer NOT NULL,
                                    price         integer NOT NULL,
                                    ship_date     text NOT NULL,
                                    FOREIGN KEY   (id) REFERENCES customers (id)
                                );"""

  # create a database connection
  conn = db_connect(dbfile)

  if conn is not None:
    create_table(conn, sql_create_customers_table)
    create_table(conn, sql_create_orders_table)
  else:
    print("CANNOT  create the database connection.")

#    insert_values, don't let the primary key id duplicate , it is PRIMARY KEY
  c = conn.cursor()
#    c.execute(" DROP TABLE customers")
  customers_data = [(1176, 'APPLE', '12/8/2000', 120000),
                    (1178, 'IBM', '12/12/2005', 240000)]
  c.executemany("INSERT INTO customers VALUES (?,?,?,?)", customers_data)
  conn.commit()
  print("\nList all the records in the table after INSERT customers:\n")
  for row_record in c.execute("SELECT * FROM customers ORDER BY id"):
    print(row_record)

  c = conn.cursor()
#    c.execute(" DROP TABLE orders")
  orders_data = [(1176, 'APPLE', 200, "AVL car L1", 100, '12/05/2016'),
                 (1178, 'IBM', 300, "AVL car L2", 150, '12/06/2015')]
  c.executemany("INSERT INTO orders VALUES (?,?,?,?,?,?)", orders_data)
  conn.commit()
  print("\nList all the records in the table after INSERT orders:\n")
  for row_record in c.execute("SELECT * FROM orders ORDER BY id"):
    print(row_record)
  print("\nList all the records in the table after SELECT:\n")
  for row_record in c.execute("SELECT * FROM orders WHERE EXISTS(SELECT * FROM customers WHERE customers.id=orders.id)"):
    print(row_record)


if __name__ == '__main__':
  main()

# %load dbformat.py
#fielname: dbformat.py
# function: sqlite3 insert data and commit using the format style
import sqlite3
import os

sqlite_file = "D:/BOOK/CHAP14/CHAP13_CUST.DB"
table_name = 'customers'
id_column = 'id'
name_column = 'cust_name'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

#c.execute("DROP TABLE IF EXISTS customers")
#c.execute("CREATE TABLE customers (Id INTEGER PRIMARY KEY , cust_name TEXT)")

# Inserts customer ID
try:
  c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (1101, 'APPLE')".
            format(tn=table_name, idf=id_column, cn=name_column))
  conn.commit()
except sqlite3.IntegrityError:
  print('**** ID exists ERROR  since it is PRIMARY KEY  {}'.format(id_column))
#    sys.exit(1)
#    if conn:
#        conn.rollback()
#    print ("Error %s:" % err.args[0])
#    sys.exit(1)


else:
  print("Sucessful")
  for row_record in c.execute("SELECT * FROM customers"):
    print(row_record)

# insert an customer ID if the ID not exist

c.execute("INSERT OR IGNORE INTO {tn} ({idf}, {cn}) VALUES (1102, 'APPLE')".
          format(tn=table_name, idf=id_column, cn=name_column))

# Updates the  inserted or existing row record's cust_name
c.execute("UPDATE {tn} SET {cn}=('IBM') WHERE {idf}=(1101)".
          format(tn=table_name, cn=name_column, idf=id_column))

conn.commit()
print("\nList all the records in the table after INSERT and Update :\n")
for row_record in c.execute("SELECT * FROM customers"):
  print(row_record)

conn.close()

# %load rollback.py
#fielname: rollback.py
# function: rollback after commit
#          it will not rollback if no commit
import sqlite3
import os

sqlite_file = "D:/BOOK/CHAP14/CUST.DB"
table_name = 'customers'
id_column = 'id'
name_column = 'cust_name'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS customers")
c.execute("CREATE TABLE customers (Id INTEGER PRIMARY KEY , cust_name TEXT,dating TEXT, credit INTEGER NOT NULL)")

# Inserts customer ID
try:

  #   c.execute("BEGIN")
  customers_data = [(1170, 'APPLE', '12/8/2000', 120000),
                    (1172, 'IBM', '12/12/2005', 240000)]
  c.executemany("INSERT INTO customers VALUES (?,?,?,?)", customers_data)
#   c.commit()

except:
  c.execute("ROLLBACK")
  print("error ROLLBACK")
else:
  print("OK")


print("\nList all the records in the table after INSERT and Update :\n")
for row_record in c.execute("SELECT * FROM customers"):
  print(row_record)

c.execute("ROLLBACK")
print("\nList all the records in the table after INSERT and Update :\n")
for row_record in c.execute("SELECT * FROM customers"):
  print(row_record)

conn.close()

# %load app_cars.py
#filename: App_cars.py
# function: use the SQLite in the application for car database

import sqlite3 as lite
import sys
dbfile = "D:/BOOK/CHAP14/CUST.DB"

con = lite.connect(dbfile)
with con:

  cur = con.cursor()
  cur.execute("DROP TABLE IF EXISTS cars")
  cur.execute(
    "CREATE TABLE cars(Id INT PRIMARY KEY, Name TEXT, MODEL TEXT DEFAULT 'normal' ,year INT)")
  cur.execute("INSERT INTO cars VALUES(1100,'BMW', 'BMW X5',1965)")
  cur.execute("INSERT INTO cars VALUES(1101,'HYYDAI','NORMAL',1965)")

  cars_data = [(1105, 'AUDI', 'A6', 1965),
               (1102, 'Mercedes', 'S3', 2001),
               (1107, 'TOYOTA', 'Camery', 2010)
               ]
  cur.executemany("INSERT INTO cars VALUES (?,?,?,?)", cars_data)


print("\nList all the records in the table after INSERT :\n")
for row_record in cur.execute("SELECT rowid, * FROM cars ORDER BY Name"):
  print(row_record)


print("\nList all the records in the table after SELECT:\n")
for row_record in cur.execute("SELECT * FROM cars WHERE Name = 'AUDI'"):
  print(row_record)

con.close()

# %load sqlite_ver.py
# filename:sqlite_ver.py
# function: to check the sqlite version

import sqlite3
import sys

con = None
dbfile = "D:/BOOK/CHAP14/CHAP13_CUST.DB"

try:
  con = sqlite3.connect('dbfile.db')
  cur = con.cursor()
  cur.execute('SELECT SQLITE_VERSION()')
  ver = cur.fetchone()

  print("SQLite3 version is as follows: %s" % ver)

except sqlite3.Error as e:

  print("Error %s:" % e.args[0])
  sys.exit(1)

else:
  print("SQLite3 version is as follows: %s" % ver)

finally:
  if con:
    con.close()

# %load employee_count.py

# filename:employee_count.py
# function: create database and create table, insert value to table

import sqlite3
dbfile = "D:/BOOK/CHAP13/employee.DB"
connection = sqlite3.connect(dbfile)

cursor = connection.cursor()

# delete the table first
cursor.execute("""DROP TABLE employee;""")

sql_CREATE_TABLE = """
CREATE TABLE employee ( 
emp_id INTEGER PRIMARY KEY, first VARCHAR(10), last VARCHAR(8), 
sex CHAR(1), hire DATE,birth DATE,salary int);
"""

cursor.execute(sql_CREATE_TABLE)

sql_INSERT = """INSERT INTO employee (emp_id, first, last, sex, hire,birth,salary)
    VALUES (1999, "Steven", "Bush", "M","2000-01-26", "1966-12-25",5000);"""
cursor.execute(sql_INSERT)

sql_INSERT = """INSERT INTO employee (emp_id, first, last, sex, hire,birth,salary)
    VALUES (1990, "John", "Hu", "M","2006-05-26", "1990-1-25",5500);"""
cursor.execute(sql_INSERT)

sql_INSERT_command = """INSERT INTO employee (emp_id, first, last, sex, hire,birth,salary)
    VALUES (2000, "Ted", "HSU", "M","1980-01-26", "1963-10-25",4000);"""
cursor.execute(sql_INSERT_command)


# use commit() when you want to save the changes
connection.commit()
cursor.execute(
  "SELECT COUNT(*) from employee where salary >4000 AND first='John'")
(number_of_rows,) = cursor.fetchone()
print("count=", number_of_rows)


connection.close()

# %load exam13-2.py
# filename:chap13_ex1_create_table
# function:check why the sytax is wrong

import sqlite3

#-------------------------db creation ---------------------------------------#
dbconn = sqlite3.connect('/my_db.db')
cursor = dbconn.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
dbconn.execute('''CREATE TABLE EMPLOYEE
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')


cursor.execute("DROP TABLE IF EXISTS IOT_table")
sql = """CREATE TABLE IOT_table (
        name        TEXT DEFAULT NULL,
        temperature INT,
        location    CHAR(50),
        );"""
cursor.execute(sql)

sql = ("CREATE INDEX index_iot_table ON IOT_table(name);")
cursor.execute(sql)

# %load exam13-3.py
# filename:sqlite_Datatype.py
# function: show the data type

import sqlite3
sql_create_cusomer_table = """
CREATE TABLE IF NOT EXISTS customer (
  Customer_id  INT  PRIMARY KEY  DEFAULT 1101,
  Cust_Name VARCHAR(10) NOT NULL DEFAULT "APPLE",
  Credit int  NOT NULL DEFAULT 10000,
  Phone   VARCHAR(10) NULL
);
"""

db_file = "D:/BOOK/CHAP14/CHAP13_TEST.DB"

try:
  conn = sqlite3.connect(db_file)
  print(conn)

except Error as err:
  print(err)
else:
  print("OK")

conn.execute(sql_create_cusomer_table)

customer_data = [(1102, "APPLE", 10000, "212-3312456"),
                 (1101, "IBM", 20000, ""),
                 (1102, "Google", 30000, "716-3222222")]
cursor = conn.cursor()
cursor.executemany("INSERT INTO customer VALUES (?,?,?,?)", customer_data)
print("\nList all the records in the table after INSERT :\n")
for row_record in cursor.execute("SELECT rowid, * FROM customer ORDER BY Customer_id"):
  print(row_record)