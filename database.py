# !!!UNCOMMENT FOR DATABASE CREATION!!!

import sqlite3

conn = sqlite3.connect("article_data.db")
# creates cursor
c = conn.cursor()

c.execute('''CREATE TABLE articles (title TEXT, href TEXT, topic TEXT, date_input TEXT)''')
# commit changes
conn.commit()
conn.close()
# conn = sqlite3.connect("rocket_data.db")
#     c = conn.cursor()
#
#     c.executemany("INSERT INTO rocket_values VALUES (?,?,?,?,?,?,?,?,?,?,?)", rocket_chars)
#     c.executemany("INSERT INTO rocket_calculations VALUES (?,?,?,?,?,?,?,?,?,?,?)", rocket_calcs)
#
#     conn.commit()
#     conn.close()