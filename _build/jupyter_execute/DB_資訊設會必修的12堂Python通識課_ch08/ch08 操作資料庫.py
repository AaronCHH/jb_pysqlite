# Ch08 操作資料庫

{cite}`資訊設會必修的12堂Python通識課_2019`

#顯示學生成績表
import sqlite3
dbfile = "school.db"
conn = sqlite3.connect(dbfile)
rows = conn.execute("select * from score;")
for row in rows:
    for field in row:
        print("{}\t".format(field), end="")
    print()
conn.close()

#輸入學生成績
import sqlite3
dbfile = "school.db"
conn = sqlite3.connect(dbfile)
stuno = input("學號：")
chi = input("國文成績：")
eng = input("英文成績：")
mat = input("數學成績：")
his = input("歷史成績：")
geo = input("地理成績：")
sql_str = "insert into score(stuno, chi, eng, mat, his, geo) values('{}',{},{},{},{},{});".format(
    stuno, chi, eng, mat, his, geo)
conn.execute(sql_str)
conn.commit()
conn.close()

#輸入學生資料表 
import sqlite3
dbfile = "school.db"
conn = sqlite3.connect(dbfile)
stuno = input("學號：")
while stuno!="-1":
    name = input("姓名：")
    gender = input("性別：")
    clsno = input("班級編號：")
    tel = input("電話：")
    pid = input("家長身份證字號：")
    sql_str = "insert into studata(stuno, name, gender, clsno, tel, pid) values('{}','{}','{}','{}','{}','{}');".format(
        stuno, name, gender, clsno, tel, pid)
    conn.execute(sql_str)
    stuno = input("學號：")
conn.commit()
conn.close()

#顯示學生基本資料表
import sqlite3
dbfile = "school.db"
conn = sqlite3.connect(dbfile)
rows = conn.execute("select * from studata;")
for row in rows:
    for field in row:
        print("{}\t".format(field), end="")
    print()
conn.close()

#顯示學生的完整成績表（含總分及平均）
import sqlite3
dbfile = "school.db"
conn = sqlite3.connect(dbfile)
rows = conn.execute("select stuno, chi, eng, mat, his, geo, chi+eng+mat+his+geo, (chi+eng+mat+his+geo)/5 from score;")
print("學號\t國文\t英文\t數學\t歷史\t地理\t總分\t平均")
for row in rows:
    for field in row:
        print("{}\t".format(field), end="")
    print()
conn.close()

#顯示學生各科的平均
import sqlite3
dbfile = "school.db"
conn = sqlite3.connect(dbfile)
rows = conn.execute("select stuno, avg(chi), avg(eng), avg(mat), avg(his), avg(geo) from score;")
print("學號\t國文\t英文\t數學\t歷史\t地理")
for row in rows:
    for field in row:
        print("{}\t".format(field), end="")
    print()
conn.close()

#依姓名顯示成績表
import sqlite3
dbfile = "school.db"
conn = sqlite3.connect(dbfile)
rows = conn.execute("select studata.name, score.chi, score.eng from score, studata;")
for row in rows:
    for field in row:
        print("{}\t".format(field), end="")
    print()
conn.close()

#依姓名顯示成績表--使用INNER JOIN
import sqlite3
dbfile = "school.db"
conn = sqlite3.connect(dbfile)
rows = conn.execute("select studata.name, score.chi, score.eng from score inner join studata on score.stuno = studata.stuno;")
for row in rows:
    for field in row:
        print("{}\t".format(field), end="")
    print()
conn.close()

#成績修改程式
import sqlite3
dbfile = "school.db"
conn = sqlite3.connect(dbfile)
stuno = input("請輸入想要修改成績的學號：")
rows = conn.execute("select stuno, chi, eng, mat, his, geo from score where stuno='{}'".format(stuno))
row = rows.fetchone()
if row is not None:
    print("學號\t國文\t英文\t數學\t歷史\t地理")
    for field in row:
        print("{}\t".format(field), end="")
    print()
chi = input("國文=")
eng = input("英文=")
mat = input("數學=")
his = input("歷史=")
geo = input("地理=")
sql_str = "update score set stuno='{}', chi={}, eng={}, mat={}, his={}, geo={} where stuno='{}';".format(
    stuno, chi, eng, mat, his, geo, stuno)
conn.execute(sql_str)
conn.commit()
conn.close()

import sqlite3
dbfile = "school.db"
conn = sqlite3.connect(dbfile)
rows = conn.execute("select * from score;")
print(type(rows))
print(dir(rows))
print(type(rows.fetchone()))
conn.close()

import sqlite3
dbfile = "school.db"
conn = sqlite3.connect(dbfile)
cur = conn.cursor()
cur.execute("select * from score;")
print(type(cur.fetchone()))
print(cur.fetchone())

import sqlite3
dbfile = "school.db"
conn = sqlite3.connect(dbfile)
cur = conn.cursor()
cur.execute("select * from score;")
first3_records = cur.fetchmany(3)
all_records = cur.fetchall()
print(first3_records)
print(all_records)
conn.close()

import sqlite3
dbfile = "school.db"
conn = sqlite3.connect(dbfile)
conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute("select * from score;")
rows = cur.fetchall()
print(rows[0].keys())
print(type(rows))
print(type(rows[0]))
print("學號\t國文\t英文")
for row in rows:
    print("{}\t{}\t{}".format(row['stuno'], row['chi'], row['eng']))