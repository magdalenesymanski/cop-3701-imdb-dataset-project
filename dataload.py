import oracledb
import csv
# Grader i am so sorry this code is being held together with hopes and dreams
# --- CONFIGURATION ---
# Path to your extracted Instant Client (Required for FreeSQL/Cloud or older oracle DB versions)
LIB_DIR = r"C:\oracle\instantclient\instantclient_23_0"

# Your Oracle Credentials
DB_USER = "HSYMANSKI10204_SCHEMA_KBVED"  # or your FreeSQL username
DB_PASS = "FCs81CFD7SYATT72I3PPUD8I16$JRB"  # your password for the dbms user
DB_DSN = "db.freesql.com:1521/23ai_34ui2"  # or your FreeSQL DSN
# jdbc:oracle:thin:@127.0.0.1:1521:XE
# 1. Initialize Thick Mode (Required for encrypted Cloud/FreeSQL connections)
if LIB_DIR:
    oracledb.init_oracle_client(lib_dir=LIB_DIR)
else:
    oracledb.enable_thin_mode()

cursor = None
conn = None
MAX_ROWS1 = 5000
MAX_ROWS2 = 100

try:
    # 2. Establish Connection
    conn = oracledb.connect(user=DB_USER, password=DB_PASS, dsn=DB_DSN)
    cursor = conn.cursor()
    print("Connected to Oracle Database")

    country_data = []
    with open("country.csv", encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)

        for row in reader:
            country_data.append([x if x != "" else None for x in row])
    cursor.executemany("INSERT INTO country VALUES (:1, :2)", country_data)
    conn.commit()
    print("Country Loaded")

    # genre
    genre_data = []
    with open("genre.csv", encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)

        for row in reader:
            genre_data.append([x if x != "" else None for x in row])
    cursor.executemany("INSERT INTO genre VALUES (:1, :2)", genre_data)
    conn.commit()
    print("Genre Loaded")

    # production company
    prod_data = []
    with open("prod_company.csv", encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)

        for row in reader:
            prod_data.append([x if x != "" else None for x in row])
    cursor.executemany("INSERT INTO production_company VALUES (:1, :2)", prod_data)
    conn.commit()
    print("Production Company Loaded")

    # cast member
    member_data = []
    with open("cast_member.csv", encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)

        for row in reader:
            for i, row in enumerate(reader):
                if i >= MAX_ROWS1:
                    break
            member_data.append([x if x != "" else None for x in row])
    cursor.executemany("INSERT INTO cast_member VALUES (:1, :2)", member_data)
    conn.commit()
    print("Cast Member Loaded")

    # title
    title_data = []
    with open("title.csv", encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)

        for row in reader:
            for i, row in enumerate(reader):
                if i >= MAX_ROWS1:
                    break
            title_data.append([x if x != "" else None for x in row])
    cursor.executemany("INSERT INTO titles VALUES (:1, :2, :3)", title_data)
    conn.commit()
    print("Titles Loaded")

    # movie
    movie_data = []
    with open("movie.csv", encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)

        for row in reader:
            for i, row in enumerate(reader):
                if i >= MAX_ROWS2:
                    break
                # fixing date formatting issue
                date = row[7]
                if len(date.strip()) == 4:
                    date = date+'01-01'
            movie_data.append([x if x != "" else None for x in row])
    cursor.executemany("""INSERT INTO movie VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15)""",movie_data)
    conn.commit()
    print("Movie Loaded")

    # movie actors
    actor_data = []
    with open("movie_actors.csv", encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)

        for row in reader:
            for i, row in enumerate(reader):
                if i >= MAX_ROWS2:
                    break
            actor_data.append([x if x != "" else None for x in row])
    cursor.executemany("INSERT INTO movie_actors VALUES (:1, :2, :3)", actor_data)
    conn.commit()
    print("Actors Loaded")

    # movie financials
    financials_data = []
    with open("movie_financials.csv", encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)

        for row in reader:
            for i, row in enumerate(reader):
                if i >= MAX_ROWS2:
                    break
            financials_data.append([x if x != "" else None for x in row])
    cursor.executemany("INSERT INTO movie_financials VALUES (:1, :2, :3, :4)", financials_data)
    conn.commit()
    print("Movie Financials Loaded")

    # movie writers
    writer_data = []
    with open("movie_writers.csv", encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)

        for row in reader:
            for i, row in enumerate(reader):
                if i >= MAX_ROWS2:
                    break
            writer_data.append([x if x != "" else None for x in row])
    cursor.executemany("INSERT INTO movie_writers VALUES (:1, :2, :3)", writer_data)
    conn.commit()
    print("Movie Writers Loaded")
finally:
    # 7. Closing connection
    cursor.close()
    conn.close()
    print("Oracle connection closed.")

