import sqlite3

with open('../lab1/movie_catalogue.sql', 'r') as sql_file:
    sql_script = sql_file.read()

db = sqlite3.connect('movie.db')
cur = db.cursor()
cur.executescript(sql_script)
db.commit()

cur.executescript("""
    INSERT INTO Movie (name, description, release_date, budget, criticscore, userscore) VALUES ("Superhero movie", "Comedy action movie with the most compelling romance story", 2008, 13000000, 86, 45);
    INSERT INTO Movie (name, description, release_date, budget, criticscore, userscore) VALUES ("Red Elephant", "Drama about hardships of prison life", 2001, 13, 67, 35);
    INSERT INTO Movie (name, description, release_date, budget, criticscore, userscore) VALUES ("Bad Breaking", "Bald guy cooking bad cookies in a critically acclaimed drama series", 2099, 18000000, 87, 95);
    INSERT INTO Movie (name, description, release_date, budget, criticscore, userscore) VALUES ("Ratman V Superape", "The most boring action movie you've seen", 2018, 320000000, 78, 55);
    INSERT INTO Movie (name, description, release_date, budget, criticscore, userscore) VALUES ("Asiatrip", "Friend group from Africa decides to go on a trip across Asian countries to meet one's true love in a typical teen comedy movie", 2005, 1200000, 64, 73);
    INSERT INTO Movie (name, description, release_date, budget, criticscore, userscore) VALUES ("Finding Meme", "Fish drama about father trying to find his lost son", 2004, 20000000, 87, 89);
    INSERT INTO Movie (name, description, release_date, budget, criticscore, userscore) VALUES ("Easy Driver", "Drama about two friends riding across the USA on a quest to find true freedom", 1965, 1900000, 88, 73);
    INSERT INTO Movie (name, description, release_date, budget, criticscore, userscore) VALUES ("Cabinet of Dr. Aibolit", "Strange murders happen in a small town after Dr. Aibolit arrived to a festival in a classic mystery movie", 1934, 18000, 96, 73);
""")

#Я извиняюсь за дальнейшее, не подумал, а времени нормально сделать не хватает
res = cur.execute("SELECT name FROM Movie")
print(res.fetchall())
res = cur.execute("SELECT budget FROM Movie WHERE release_date > 2000 ORDER BY release_date ASC")
print(res.fetchall())
res = cur.execute("SELECT name FROM Movie ORDER BY userscore DESC")
print(res.fetchall())
res = cur.execute("SELECT name, (userscore - criticscore) FROM Movie")
print(res.fetchall())
res = cur.execute("SELECT name, max((userscore + criticscore) / 2) AS average_score FROM Movie")
print(res.fetchall())
res = cur.execute("""SELECT name, description FROM Movie WHERE description LIKE "%ACTION%" """)
print(res.fetchall())
res = cur.execute("""SELECT name, description, ((userscore + criticscore) / 2) AS average_score FROM Movie WHERE description LIKE "%DRAMA%" AND average_score > 85 """)
print(res.fetchall())
res = cur.execute("SELECT budget, (userscore - criticscore) FROM Movie ORDER BY budget ASC")
print(res.fetchall())

db.close()