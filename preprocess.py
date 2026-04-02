import oracledb
import csv

file = r"C:\Users\hsyma\OneDrive\Desktop\School Stuff\Assignments\Database 1\partd\IMDb movies.csv"

# tedium
country_f = open("country.csv", "w", newline='', encoding='utf-8')
genre_f = open("genre.csv", "w", newline='', encoding='utf-8')
cast_member_f = open("cast_member.csv", "w", newline='', encoding='utf-8')
title_f = open("title.csv", "w", newline='', encoding='utf-8')
prod_company_f = open("prod_company.csv", "w", newline='', encoding='utf-8')
movie_f = open("movie.csv", "w", newline='', encoding='utf-8')
movie_financials_f = open("movie_financials.csv", "w", newline='', encoding='utf-8')
actor_f = open("movie_actors.csv", "w", newline='', encoding='utf-8')
writer_f = open("movie_writers.csv", "w", newline='', encoding='utf-8')

country_w = csv.writer(country_f)
genre_w = csv.writer(genre_f)
cast_member_w = csv.writer(cast_member_f)
title_w = csv.writer(title_f)
prod_company_w = csv.writer(prod_company_f)
movie_w = csv.writer(movie_f)
movie_financials_w = csv.writer(movie_financials_f)
actor_w = csv.writer(actor_f)
writer_w = csv.writer(writer_f)

country_w.writerow(["country_id", "country"])
genre_w.writerow(["genre_id", "genre"])
cast_member_w.writerow(["member_id", "member"])
title_w.writerow(["title_id", "title", "original_title"])
prod_company_w.writerow(["company_id", "company_name"])
movie_w.writerow(["imdb_title_id", "country_id", "genre_id",
                  "company_id", "title_id", "year", "description",
                  "duration", "language",
                  "director", "avg_votes", "amt_votes",
                  "metascore", "user_reviews", "critic_reviews"])
movie_financials_w.writerow(["imdb_title_id", "usa_gross",
                             "worldwide_gross", "budget"])
actor_w.writerow(["member_id", "imdb_title_id", "role_name"])
writer_w.writerow(["writer_id", "imdb_title_id", "writer"])

countries = []
genres = []
prod_companies = []
actors = []

country_id = 1
genre_id = 1
cast_member_id = 1
title_id = 1
company_id = 1
writer_id = 1

with open(file,encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        # row 0 is always imdb id
        imdb_title_id = row[0]

        # For the life of me i wasnt able to populate country and genre with data.. please have mercy.. im sorry for spaghetti code
        # write country
        if row[7]:
            country_list = row[7].split(",")
            for c in country_list:
                if c not in countries:
                    countries.append(c.strip())
                    country_w.writerow([country_id, c.strip()])
                    country_id += 1
                c_id = countries.index(c.strip()) + 1

        # write genre
        genre = row[5].split(",")[0] if row[5] else ""
        if genre not in genres:
            genres.append(genre)
            genre_w.writerow([genre_id, genre])
            genre_id += 1
        g_id = genres.index(genre) + 1

        # write production company
        prod_company = row[11] if row[11] else ""
        if prod_company not in prod_companies:
            prod_companies.append(prod_company)
            prod_company_w.writerow([company_id, prod_company])
            company_id += 1
        pc_id = prod_companies.index(prod_company) + 1

        # write titles
        title_w.writerow([title_id, row[1], row[2]])

        # write movie
        movie_w.writerow([imdb_title_id, c_id, g_id, pc_id, title_id,
                          row[3], row[13], row[6], row[8], row[9], row[14], row[15], row[19], row[20], row[21]
        ])

        # write movie financials
        movie_financials_w.writerow([imdb_title_id, row[16], row[17], row[18]])

        # create movie actor relation (populate "role" col with "actor" because there is no role data)
        if row[12]:
            actor_names = row[12].split(",")
            for actor in actor_names:
                actor = actor.strip()
                if actor not in actors:
                    actors.append(actor)
                    cast_member_w.writerow([cast_member_id, actor])
                    cast_member_id += 1
                a_id = actors.index(actor) + 1
                actor_w.writerow([a_id, imdb_title_id, "actor"])
        title_id += 1

        if row[10]:
            writer_names = row[10].split(",")
            for w in writer_names:
                writer_w.writerow([writer_id, imdb_title_id, w.strip()])
                writer_id += 1

country_f.close()
genre_f.close()
cast_member_f.close()
title_f.close()
prod_company_f.close()
movie_f.close()
movie_financials_f.close()
writer_f.close()
actor_f.close()