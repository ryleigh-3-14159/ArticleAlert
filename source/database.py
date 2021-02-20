
import sqlite3

conn = sqlite3.connect("article_data.db")
# creates cursor
c = conn.cursor()

c.execute('''CREATE TABLE articles (title TEXT, href TEXT, topic TEXT, date_input TEXT)''')
# commit changes
conn.commit()
conn.close()
