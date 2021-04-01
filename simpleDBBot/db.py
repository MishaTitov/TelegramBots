import psycopg2
from config import HOST, DB_NAME, DB_USER, DB_PASS


__con = None


async def create_table():
    con = open_con()
    cur = con.cursor()
    cur.execute("create table if not exists items("
                "id integer primary key,"
                "name varchar not null,"
                "price integer check (price >= 0))")
    con.commit()
    cur.close()


def open_con():
    global __con
    if __con is None:
        __con = psycopg2.connect(
            host=HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
        )
    return __con


async def close_con():
    global __con
    if __con is not None:
        __con.close()


async def add_item(id: int, name: str, price: int):
    con = open_con()
    cur = con.cursor()
    cur.execute("insert into items (id, name, price) values (%s, %s, %s) returning id;",
                (id, name, price))
    id = cur.fetchone()
    con.commit()
    cur.close()
    return id[0]


async def remove_item(id: int):
    con = open_con()
    cur = con.cursor()
    cur.execute(f"delete from items where id={id} returning 1;")
    id = cur.fetchone()
    con.commit()
    cur.close()
    return id[0]


async def show_items():
    con = open_con()
    cur = con.cursor()
    cur.execute("select * from items")
    rows = cur.fetchall()
    table = ""
    for row in rows:
        table += f"id: {row[0]} name: {row[1]} price: {row[2]}\n"
    cur.close()
    return table
