import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_game(conn,game):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = '''INSERT OR IGNORE INTO games(name,price,old_price,discount,link,image,available) VALUES(?,?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, game)
    conn.commit()
    return cur.lastrowid

if __name__ == '__main__':
    conn = create_connection("boardgames.db")
    table = """ CREATE TABLE IF NOT EXISTS games (name text,price real ,old_price real ,discount real ,link text PRIMARY KEY,image text,available text); """
    example = ("Ejemplo",15.22,22.55,15,"Soy un link","soy una imagen","disponible")
    create_table(conn,table)
    print(create_game(conn,example))
