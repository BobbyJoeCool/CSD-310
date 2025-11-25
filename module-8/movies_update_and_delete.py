# Breutzmann, Robert
# CSD 310 - Database Development and Use
# Due Date 11/30/2025

""" import statements """
import mysql.connector # to connect
from mysql.connector import errorcode

import dotenv # to use .env file
from dotenv import dotenv_values

#using our .env file
secrets = dotenv_values(".env")

""" database config object """
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True #not in .env file
}

def get_studio(cur, studio):
    cur.execute(
    "SELECT studio_id FROM studio WHERE studio_name = %s",
    (studio,)
    )
    result = cur.fetchone()
    return result[0] if result else None
    
def get_genre(cur, genre):
    cur.execute(
        "SELECT genre_id FROM genre WHERE genre_name = %s",
        (genre,)
        )
    result = cur.fetchone()
    return result[0] if result else None
    
def film_exists(cur, title):
    cur.execute(
        "SELECT film_id FROM film WHERE film_name = %s",
        (title,)
    )
    return cur.fetchone() is not None

def show_films(cursor, title): # Shows all films in the Database
    cursor.execute("""
            SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film 
            INNER JOIN genre ON film.genre_id=genre.genre_id 
            INNER JOIN studio ON film.studio_id=studio.studio_id"""
        )

    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudioName: {}\n".format(film[0], film[1], film[2], film[3]))

def insert_studio(cur, db, studioName): # Inserts a new Studio to the Database
    if not get_studio(cur, studioName):
        cur.execute("""
            INSERT INTO studio (studio_name)
            VALUES (%s)
            ON DUPLICATE KEY UPDATE studio_name = studio_name
            """(studioName,)
            )
        db.commit()
        print(f"Added Studio {studioName} to the database.")
    else:
        print(f"Studio {studioName} already exists in database (skipped adding).")        

def insert_genre(cur, db, genreName): #Inserts a new Genre to the database
    if not get_genre(cur, genreName):
        cur.execute("""
            INSERT INTO genre (genre_name) 
            VALUES (%s)
            """(genreName,)
            )
        db.commit()
        print(f"Added Genre {genreName} to the database.")
    else:
        print(f"Genre {genreName} already exists in database (skipped adding).")

def insert_film(cur, db, film_name, film_releaseDate, film_runtime, film_director, genre, studio):
    studio_id = get_studio(cur, studio) # fetches the Studio ID from the given Studio
    genre_id = get_genre(cur, genre) # fetches the Genre ID from the given Genre
    
    if not studio_id: # Checks to be sure the studio exists
        print(f"ERROR: Studio-{studio} not found.")
    elif not genre_id: # Checks to be sure the Genre exists
        print(f"ERROR: Genre-{genre} not found.")
    elif not film_exists(cur, film_name): # Makes sure the film name doesn't already exist in the database
        
        # Creates a tuple to insert into the database of the given information.
        newFilm = (film_name, film_releaseDate, film_runtime, film_director, genre_id, studio_id)

        cur.execute("""
                INSERT IGNORE INTO film (film_name, film_releaseDate, film_runtime, film_director, genre_id, studio_id)
                VALUES (%s, %s, %s, %s, %s, %s)
                """, newFilm
        )
        db.commit() # Don't forget to commit the data to the database!

        # Get the new film ID assigned by the Database.
        cur.execute("SELECT film_id FROM film WHERE film_name = %s",
            (film_name,)
        )
        filmID = cur.fetchone() 

        # Print a statement that shows that the information was added
        print(f"""Added the following film to the database:
            Film Name: {film_name} ({filmID})
            Release Date {film_releaseDate}
            Runtime: {film_runtime} minutes
            Director: {film_director}
            Genre: {genre} ({genre_id})
            Studio: {studio} ({studio_id})"""
        )
    
    else:
        print("Movie already in the Database")

def change_film_genre(cur, db, film, newGenre):
    if film_exists(cur, film):
        insert_genre(cur, db, newGenre)
        genreID = get_genre(cur, newGenre)
        cur.execute("""UPDATE film
                    SET genre_id = %s
                    WHERE film_name = %s
                    """, (genreID, film)
        )
        db.commit()
        print(f"The Genre of {film} has been changed to {newGenre}")
    else:
        print(f"{film} does not exist.")

def delete_film(cur, db, film): # This will delete a film from the database.
    if film_exists(cur, film):
        sure = input(f"IMPORTANT! This will delete {film} from the Database!\nAre you sure? (y/n)")
        if sure[0].lower().strip() == "y":
            cur.execute("SELECT film_id FROM film WHERE film_name = %s", (film,))
            filmID = cur.fetchone()[0]
            cur.execute("""
                    DELETE FROM film
                    WHERE film_id = %s
                    """, (filmID,)
            )
            db.commit()
            print(f"{film} has been removed from the database")
        else:
            print("Delete Canceled")
    else:
        print(f"ERROR: {film} not found.")

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the movies database
    cur = db.cursor()
    
    # output the connection status 
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    # Part 1
    # show_films(cur, "DISPLAYING FILMS")

    # Part 2
    # insert_genre(cur, db, "Fantasy Adventure")
    # insert_studio(cur, db, "Warner Brothers")
    # insert_film(cur, db, "A Minecraft Move", 2025, 101, "Jared Hess", "Fantasy/Adventure", "Warner Brothers")
    # show_films(cur, "DISPLAYING FILMS AFTER UPDATE")

    # Part 3
    # change_film_genre(cur, db, "Alien", "Horror")
    # show_films(cur, "DISPLAYING FILMS AFTER UPDATE -Changed Alien to Horror-")

    # Part 4
    # delete_film(cur, db, "Gladiator")
    # show_films(cur, "DISPLAYING FILMS AFTER DELETE")

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """
    db.close()
