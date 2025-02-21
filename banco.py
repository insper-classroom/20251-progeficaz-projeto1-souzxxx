import sqlite3 as sql
con = sql.connect('banco.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS texto')
sql = '''CREATE TABLE texto ('id' INTEGER PRIMARY KEY, 'titulo' TEXT, 'detalhes' TEXT)'''
cur.execute(sql)
con.commit()
con.close()
