import sqlite3

with open('../lab1/movie_catalogue.sql', 'r') as sql_file:
    sql_script = sql_file.read()

def print_and_execute(cur, command):
    res = cur.execute(command)
    print(res.fetchall())

db = sqlite3.connect('movie.db')
cur = db.cursor()
cur.executescript(sql_script)
db.commit()

cur.executescript("""
    INSERT INTO Movie (name, description, release_date, budget, criticscore, userscore) VALUES ("Superhero movie", "Comedy action movie with the most compelling romance story", 2008, 13000000, 45, 86);
    INSERT INTO Movie (name, description, release_date, budget, criticscore, userscore) VALUES ("Red Elephant", "Drama about hardships of prison life", 2001, 13, 35, 67);
    INSERT INTO Movie (name, description, release_date, budget, criticscore, userscore) VALUES ("Bad Breaking", "Bald guy cooking bad cookies in a critically acclaimed drama series", 2099, 480000000, 95, 87);
    INSERT INTO Movie (name, description, release_date, budget, criticscore, userscore) VALUES ("Ratman V Superape", "The most boring action movie you've seen", 2018, 320000000, 78, 55);
    INSERT INTO Movie (name, description, release_date, budget, criticscore, userscore) VALUES ("Asiatrip", "Friend group from Africa decides to go on a trip across Asian countries to meet one's true love in a typical teen comedy movie", 2005, 1200000, 64, 73);
    INSERT INTO Movie (name, description, release_date, budget, criticscore, userscore) VALUES ("Finding Meme", "Fish drama about father trying to find his lost son", 2004, 20000000, 87, 89);
    INSERT INTO Movie (name, description, release_date, budget, criticscore, userscore) VALUES ("Easy Driver", "Drama about two friends riding across the USA on a quest to find true freedom", 1965, 1900000, 88, 73);
    INSERT INTO Movie (name, description, release_date, budget, criticscore, userscore) VALUES ("Cabinet of Dr. Aibolit", "Strange murders happen in a small town after Dr. Aibolit arrived to a festival in a classic mystery movie", 1934, 18000, 96, 73);
""")

cur.executescript("""
    INSERT INTO ActorsTable (item_id, actors_name) VALUES (1, "Aboba Jones");
    INSERT INTO ActorsTable (item_id, actors_name) VALUES (1, "Gennady Chernetsov");
    INSERT INTO ActorsTable (item_id, actors_name) VALUES (1, "Prad Bitt");
    INSERT INTO ActorsTable (item_id, actors_name) VALUES (1, "Good Saulman");
    INSERT INTO ActorsTable (item_id, actors_name) VALUES (1, "Pavel Ivlev");
    INSERT INTO ActorsTable (item_id, actors_name) VALUES (2, "Pavel Ivlev");
    INSERT INTO ActorsTable (item_id, actors_name) VALUES (3, "Aboba Jones");
    INSERT INTO ActorsTable (item_id, actors_name) VALUES (3, "King Arthur");
    INSERT INTO ActorsTable (item_id, actors_name) VALUES (3, "Vitya AK-47");
""")

cur.executescript("""
    INSERT INTO Users (username, password, email) VALUES ("Sarkoxed", "78787878", "sarkoxed@kmail.com");
    INSERT INTO Users (username, password, email) VALUES ("ne_bknn", "87878787", "nebknn@kmail.com");
    INSERT INTO Users (username, password, email) VALUES ("anzan", "iloveabba", "anzan@kmail.com");
""")

cur.executescript("""
    INSERT INTO UserReview (item_id, user_id, review_body) VALUES (1, 1, "best superhero movie i've seen after Ratman V Superape");
    INSERT INTO UserReview (item_id, user_id, review_body) VALUES (1, 3, "the only good superhero movie");
    INSERT INTO UserReview (item_id, user_id, review_body) VALUES (3, 2, "better rim kim");
    INSERT INTO UserReview (item_id, user_id, review_body) VALUES (4, 1, "the only reason i could watch this movie is because i physically cannot fall asleep");
""")

cur.executescript("""
    INSERT INTO ReviewTable (item_id, critic_name, review_body) VALUES (1, "IKN", "why would you joke about funny things??? 4.5/10")
""")

print_and_execute(cur, """SELECT name FROM Movie WHERE item_id IN (SELECT item_id FROM UserReview WHERE user_id IN (SELECT user_id FROM Users WHERE username="Sarkoxed")) """)
print_and_execute(cur, """SELECT name, ((userscore + criticscore) / 2) AS avg_score FROM Movie WHERE item_id IN (SELECT item_id FROM ActorsTable WHERE actors_name="Aboba Jones") """)
print_and_execute(cur, """SELECT Movie.name, ActorsTable.actors_name FROM Movie, ActorsTable WHERE ActorsTable.item_id = Movie.item_id ORDER BY Movie.name """)
print_and_execute(cur, """SELECT (Movie.userscore - Movie.criticscore), Users.username, UserReview.review_body FROM Movie, UserReview, Users WHERE Movie.item_id IN (SELECT item_id FROM ReviewTable WHERE critic_name="IKN") AND UserReview.item_id = Movie.item_id AND Users.user_id = UserReview.user_id""")
print_and_execute(cur, """SELECT Movie.name, ActorsTable.actors_name FROM Movie, ActorsTable GROUP BY ActorsTable.actors_name HAVING Movie.criticscore = max(Movie.criticscore)""")
print_and_execute(cur, """SELECT name FROM Movie WHERE item_id IN (SELECT item_id FROM ActorsTable WHERE actors_name = "Pavel Ivlev") ORDER BY ((Movie.userscore + Movie.criticscore) / 2) DESC""")
print_and_execute(cur, """SELECT name, userscore FROM Movie WHERE EXISTS (SELECT user_id FROM UserReview WHERE UserReview.item_id = Movie.item_id) ORDER BY userscore DESC """)
print_and_execute(cur, """SELECT email FROM Users WHERE user_id IN (SELECT user_id FROM UserReview WHERE item_id IN (SELECT item_id FROM Movie WHERE name = "Superhero movie"))""")

db.close()