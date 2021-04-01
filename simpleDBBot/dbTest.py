import psycopg2


#connecting to the db
con = psycopg2.connect(
    host="localhost",
    database="myTestdb",
    user="postgres",
    password="gvr591",
    port=5432
)
#cursor
cur = con.cursor()

#work with db
# table_str = "create table items (id integer primary key, name varchar, quantity integer);"
# insert_str = "insert into items values(1, 'item1', 100), (2, 'item2', 100), (3, 'item3', 100);"
# cur.execute(table_str)
# cur.execute(insert_str)
# con.commit()
# cur.close()
#
# cur = con.cursor()
#
# cur.execute("insert into items (id, name, quantity) values (%s, %s, %s)", (4, "item4", 200))
cur.execute("drop table items;")
con.commit()
#close the cursor
cur.close()
#close the connection
con.close()