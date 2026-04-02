BEGIN
  FOR c IN (SELECT table_name FROM user_tables) LOOP
    EXECUTE IMMEDIATE ('DROP TABLE ' || c.table_name || ' CASCADE CONSTRAINTS');
  END LOOP;
END;
/
PURGE RECYCLEBIN;

SELECT tablespace_name, bytes, max_bytes
FROM user_ts_quotas;

CREATE TABLE country (
    country_id NUMBER PRIMARY KEY,
    country VARCHAR(100)
);

CREATE TABLE genre (
    genre_id NUMBER PRIMARY KEY,
    genre VARCHAR(100)
);

CREATE TABLE cast_member (
    member_id NUMBER PRIMARY KEY,
    member VARCHAR(100)
);

CREATE TABLE titles (
    title_id NUMBER PRIMARY KEY,
    title VARCHAR(100),
    original_title VARCHAR(100)
);

CREATE TABLE production_company (
    company_id NUMBER PRIMARY KEY,
    company_name VARCHAR(500)
);

CREATE TABLE movie (
    imdb_title_id VARCHAR(20) PRIMARY KEY,
    country_id NUMBER,
    genre_id NUMBER,
    company_id NUMBER,
    title_id NUMBER,
    year NUMBER,
    description VARCHAR(1000),
    duration NUMBER,
    language VARCHAR(100),
    director VARCHAR(100),
    avg_votes NUMBER,
    amt_votes NUMBER,
    metascore NUMBER,
    user_reviews NUMBER,
    critic_reviews NUMBER

    /* 
        It is necessary that I remove all foreign key contraints from any relations following the prod_company relation,
        as the data limit that freesql imposes makes it impossoble to load all 80k+ records of my dataset, meanwhile
        many relations require all of the data to be loaded in order to reference foreign keys from another table.
        An impossible thing to remedy without starting over completely, I just made the decision to comment out the foreign 
        key references in order to prevent the error in the dataload.py file.
    */
    /*
    CONSTRAINT fk_movie_country
    FOREIGN KEY (country_id) REFERENCES country(country_id),
    CONSTRAINT fk_movie_genre
    FOREIGN KEY (genre_id) REFERENCES genre(genre_id),
    CONSTRAINT fk_movie_company
    FOREIGN KEY (company_id) REFERENCES production_company(company_id),
    CONSTRAINT fk_movie_titles
    FOREIGN KEY (title_id) REFERENCES titles(title_id)
    */
);

CREATE TABLE movie_financials (
    imdb_title_id VARCHAR(20) PRIMARY KEY,
    usa_gross VARCHAR(20),
    worldwide_gross VARCHAR(20),
    budget VARCHAR(20)

    /*
    CONSTRAINT fk_financials_movie
    FOREIGN KEY (imdb_title_id) REFERENCES movie(imdb_title_id)
    */
);

CREATE TABLE movie_actors (
    member_id NUMBER,
    imdb_title_id VARCHAR(20),
    role_name VARCHAR(100),

    CONSTRAINT pk_ma
    PRIMARY KEY (member_id, imdb_title_id)

    /*
    CONSTRAINT fk_ma_member
    FOREIGN KEY (member_id) REFERENCES cast_member(member_id),
    CONSTRAINT fk_ma_movie
    FOREIGN KEY (imdb_title_id) REFERENCES movie(imdb_title_id)
    */
);

CREATE TABLE movie_writers (
    writer_id NUMBER PRIMARY KEY,
    imdb_title_id VARCHAR(20),
    writer VARCHAR(100)
    /*
    CONSTRAINT fk_mw_movie
    FOREIGN KEY (imdb_title_id) REFERENCES movie(imdb_title_id)
    */
);
