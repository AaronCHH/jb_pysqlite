# Ch13 使用 sqlite3 模組管理 SQLite 資料庫

{cite}`Python程式設計_2016`

import sqlite3
con = sqlite3.connect('school.db')
cur = con.cursor()

# cur.execute('DROP TABLE stu')

sql1 = '''CREATE TABLE IF NOT EXISTS stu ( 
        stuid   INTEGER       PRIMARY KEY, 
        name   VARCHAR(50)   not null, 
        pid     VARCHAR(20)   not null, 
        phone   VARCHAR(20)   not null)'''
cur.execute(sql1)

sql2 = "INSERT INTO stu VALUES (104001,'Claire','B342222','1245667')"
cur.execute(sql2)

record = (104002, 'Marry', 'B342223', '1245668')
sql3 = 'INSERT INTO stu VALUES(?,?,?,?)'
cur.execute(sql3, record)

cur.execute('SELECT * FROM stu')
rows = cur.fetchall()

print(rows)
con.commit()
con.close()

