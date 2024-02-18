import sqlite3

database=conn=sqlite3.connect('C:/kevin/mydb.db')
cursor=conn.cursor()
#cursor.execute("select cu.cuid,cunam, oda.odaid from cu left join oda on cu.cuid=oda.odaid")
cursor.execute("select * from cu")
rows=cursor.fetchall()
for row in rows:
#    cuid,cunam,odaid=row
    cuid, cunam = row
#    print(f"Customer id:{cuid},Name: {cunam}, order id: {odaid}")
    print(f"Customer id:{cuid}, Name: {cunam}")
cursor.close()
conn.close()
