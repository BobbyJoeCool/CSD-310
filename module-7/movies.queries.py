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

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the movies database
    cur = db.cursor()
    
    # output the connection status 
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    # Query 1 - All Studio Records
    cur.execute("SELECT * FROM studio")
    rows1 = cur.fetchall()
    print("")
    print("--DISPLAYING Studio RECORDS--")
    for row in rows1:
        print(f"Studio ID: {row[0]}")
        print(f"Studio Name: {row[1]}")
        print("")

    # Query 2 - All Genre Records
    cur.execute("SELECT * FROM genre")
    rows2 = cur.fetchall()
    print("")
    print("--DISPLAYING Genre RECORDS--")
    for row in rows2:
        print(f"Genre ID: {row[0]}")
        print(f"Genre Name: {row[1]}")
        print("")

    # Query 3 - Select the movie names for those movies that have a run time of less than two hours.
    cur.execute("SELECT * FROM film WHERE film_runtime < 120;")
    rows3 = cur.fetchall()
    print("")
    print("--DISPLAYING Short Film RECORDS--")
    for row in rows3:
        print(f"Film Name: {row[1]}")
        print(f"Runtime: {row[3]} minutes")
        print("")
    
    # Query 4 - Get a list of film names, and directors grouped by director.
    cur.execute("SELECT * FROM film ORDER BY film_director;")
    rows4 = cur.fetchall()
    print("")
    print("--DISPLAYING Director RECORDS in Order--")
    for row in rows4:
        print(f"Film Name: {row[1]}")
        print(f"Director: {row[4]} ")
        print("")

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