CREATE TABLE IF NOT EXISTS Movie (
    item_id integer PRIMARY KEY,
    name string,
    description text,
    release_date integer,
    budget integer,
    userscore integer,
    criticscore integer
);

CREATE TABLE IF NOT EXISTS Users (
    user_id integer PRIMARY KEY,
    username string,
    password string,
    email string UNIQUE
);

CREATE TABLE IF NOT EXISTS UserReview (
    id integer PRIMARY KEY,
    item_id integer,
    user_id integer,
    review_body text,

    FOREIGN KEY(item_id) REFERENCES Movie(item_id),
    FOREIGN KEY(user_id) REFERENCES Users(user_id)
);

CREATE TABLE IF NOT EXISTS MovieCatalogue (
    id integer PRIMARY KEY,
    item_id integer,
    link string,

    FOREIGN KEY(item_id) REFERENCES Movie(item_id)
);

CREATE TABLE IF NOT EXISTS ActorsTable (
    id integer PRIMARY KEY,
    item_id integer,
    actors_name string,

    FOREIGN KEY(item_id) REFERENCES Movie(item_id)
);

CREATE TABLE IF NOT EXISTS ReviewTable (
    id integer PRIMARY KEY,
    item_id integer,
    critic_name string,
    review_body text,

    FOREIGN KEY(item_id) REFERENCES Movie(item_id)
);