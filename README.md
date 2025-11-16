# CSD-310
Database Development and Use

## Module 1
10/20/2025 - 10/26/2025

Welcome to Module 1! In this module, we will be exploring why and how data is stored. We will also begin the task of determining how to decide how a database is organized (the schema), and what constitutes an entity (table) and what is meant by a relationship between entities. Lastly, you'll be setting up the repository you'll be needing for the course.

### Deliverables
1) Module 1.1 Discussion Board Initial Post - Due by Thursday 11:59 p.m., CST.
2) Discussion Board Responses - Due by Sunday 11:59 p.m., CST.
3) Module 1.2 Assignment: GitHub Repository Setup - Due by Sunday 11:59 p.m., CST.
4) Module 1.3 Assignment: Basic Comparison of Relational vs. NoSQL Databases - Due by Sunday 11:59 p.m., CST.

### Discussion Board
For this module's discussion board assignment, examine your own daily routine for at least two days. After reading the chapter, compile a list of all the possible databases you may have interacted with. Don't forget to include mobile devices and possible cloud environments. Were you surprised at how many are on the list? In your response to others, comment on whether the list was missing any obvious items, or whether some items are, in fact, database related.

### Assignments
#### Assignment 1.2
For this module’s assignment, we will be creating a GitHub repository using git and the command line interface (CLI). The repository we create in this assignment will be used throughout the course to host the coding assignments. If you have not already installed git , please do so before continuing. Make sure that you include the steps to set the global username and global email address.

There are resources available in the Git/GitHub Resources menu item to the left on installing and configuring Git.

**Instructions:**

1) Click on each instruction box below to expand the instructions.
2) Complete the setup instructions and save the following items into a single word document:
    - Link to your GitHub repository
    - Screenshot of your GitHub repository
    - Screenshot of your local directory, following the structure format provided in the instructions below.

**Deliverables:**
1) Link to your GitHub repository.
2) Screenshot of your GitHub repository.
3) Screenshot of your local directory (properly formatted).
4) Combine all 3 items into a single word document and title it "your-last-name"-"assignment-name".docx.

#### Assignment 1.3
Create a Word document that addresses the following:

1) In the context of relational databases, what are relationships? Describe at least two, and provide an example of their use.
2) What are the advantages of relational databases? What are the advantages of NoSQL databases?
3) What are the disadvantages of relational databases? What are the disadvantages of NoSQL databases?
4) Identify at least two features of MySQL and two features of MongoDB, and describe what they are and how they are used.

## Module 2
10/27/2025 - 11/2/2025

Welcome to Module 2! During this module, we will exploring data models associated with both relational and NoSQL databases. We will also be working with Visual Paradigm, an online ERD modeling tool.

### Deliverables

1) Module 2.1 Discussion Board Initial Post - Due by Thursday 11:59 p.m., CST.
2) Discussion Board Responses - Due by Sunday 11:59 p.m., CST.
3) Module 2.2 Assignment: Visual Paradigm - Due by Sunday 11:59 p.m., CST.
4) Module 2.3 Assignment: Data Models - Due by Sunday 11:59 p.m., CST.

### Discussion Board
For this module’s discussion board assignment respond to one the following topics:
1) Explain the primary purpose for constructing a data model for a database. Is a data model always necessary? Why or why not?
2) What are business rules? And how do they relate to creating data models? Provide an example.
3) What is the difference between an Entity Relationship Diagram and an Object Relationship Diagram? Provide an example of when you might use each.
4) What is cardinality in data modeling? How many types of cardinality depiction are there? Which would you prefer and why?

### Assignments
#### Assignment 2.2
For this assignment, you are to practice using Visual Paradigm to create an ERD.

**Instructions:**

1) Create (if you haven't already) a directory in CSD-310 named module-2.
2) Go out to the link above for "Visual Paradigm Online ERD Tool". Before you begin, you may want to watch the Visual Paradigm Tutorial Video for pointers. Your task is to re-create this ERD. (See picture in Blackboard)
3) Once you've finished, either take a screenshot, or download the graphic, paste it into a Word document, add your name and the assignment number at the top of the first page.
4) Save your document as "your-last-name"-"assignment-name".docx into your CSD-310/module-2 directory.
5) Stage, commit, and push your work to GitHub.

**Deliverables**

1) Word document with your name and assignment number on first page, with screenshot or graphic of ERD.

#### Assignment 2.3
For this week's assignment we will be comparing and contrasting the differences between relational and non-relational database structures.

Relational databases have been a successful technology for over twenty years, providing persistence, concurrency control, and an integration mechanism (Fowler & Sadalage, 2012). Data persistence, as the name suggests, is the process of persisting data to some physical location. The popularity of relational databases derives from its ability to make-sense of complex data structures. Data is categorized into tables, columns, and rows. Tables represent the entities (think JavaScript classes), columns represent the Meta data (think JavaScript properties), and rows are the raw data elements (think values). There are three types of relationships in a relational database system, One-to-Many, Many-to-Many, and One-to-One. Business rules are brief, precise, and unambiguous descriptions of a policy, procedure, or principle within an organization. Diagrams are used to graphically illustrate these business rules and their associated relationships. (See Blackboard for the diagrams.)

There is a movement away from using databases as integration points towards encapsulating databases within applications and integrating through services (Fowler & Sadalage, 2012). This gravitation has resulted in the adoption and evolution of NoSQL database structures. Web communications and transmissions are unstructured data components that require a mechanism for dealing with their complexities. NoSQL technologies bridge this gap by not forcing developers into specific paradigms, rather allowing them to keep the data generic and language agnostic. In a NoSQL world, the above diagrams data structure may resemble the following:

    NoSQL Data Structure:
    {
    "first_name": "Martin",
    "last_name": "Fowler",
    "cars": [
    {
    "type": "Ford",
    "color": "White"
    },
    {
    "type": "Nissan",
    "color": "Black"
    }
    ]
    }

The key point here is, CARs is a nested collection under the USER document.

**Instructions:**
1) Create (if you haven't already) a directory in CSD-310 named module-2.
2) Translate the following business rules into one Entity relationship diagram (ERD) using Visual Paradigm.
    - a USER has many ROLES.
    - a USER has one BIRTHDATE.
    - a USER can have many DEPENDENTS.
3) Convert the translated diagram into one NoSQL data structure.
4) Save the ERD and NoSQL data structure as separate image files.
5) Combine the images into a single Word document, add your name and the assignment number at the top of the first page.
6) Save your document as "your-last-name"-"assignment-name".docx into your CSD-310/module-2 directory.
7) Stage, commit, and push your work to GitHub.

**Deliverables**
1) Word document with your name and assignment number on first page, with screenshot or graphic of ERD and one of NoSQL data structure.

## Module 3
11/3/2025-11/9/2025

Welcome to Module 3! During this module, we will exploring data models associated with both relational and NoSQL databases. We will also be working with Visual Paradigm, an online ERD modeling tool.

### Deliverables

1) Module 3.1 Discussion Board Initial Post - Due by Thursday 11:59 p.m., CST.
2) Discussion Board Responses - Due by Sunday 11:59 p.m., CST.
3) Module 3.2 Assignment: Normalized Tables - Due by Sunday 11:59 p.m., CST.

### Discussion Board
**Discussion Question: Normalization**


For this module's discussion board assignment respond to one the following topics:

1) Can a database be in Third Normal Form (3NF), without achieving First Normal Form (1NF)? Why or why not?
2) At what point can the data in a field be considered atomic? Is it possible to carry atomicity too far and how do you know this has happened? Provide an example not found in the text.
3) What is the purpose of a foreign key? Can you have more than one? Provide an example.
4) In an employee database would you store a person's physical age, their date of birth or both? Why or why not?

### Assignments

Assignment: Normalized Tables
For this assignment, you are to take a set of fields and categorize them appropriately into tables and then ensure those tables are in 3NF. There is no one correct solution to this, so you should include any assumptions you make. The solution should be in table/cell format, not in an ERD format. This is an example of moving from 1NF to 3NF in a table/cell format.

The first image below is a possible solution for student, faculty and other data fields and how they might be organized into tables. (See Blackboard fot Images)

Assignment Data Fields:
- publisher_name
- publisher_ID
- publisher_address
- book_isbn
- book_name
- book_price
- author_first_name
- author_last_name
- author_phone
- author_email
- publisher_email
- author_address

**Instructions:**
1) Create (if you haven't already) a directory in CSD-310 named module-3.
2) Take the Assignment Data Fields and organize them into tables, then get those tables into 3rd Normal Form (3NF). You do not have to use Excel, but the result should be similar to the above. Once you've finished, either embed the Excel sheet in a Word document or take a screenshot and paste it into a Word document. Make sure your name and assignment number are at the top of the Word document.
3) Save your document as "your-last-name"-"assignment-name".docx into your CSD-310/module-3 directory.

## Module 4
11/10/2025 - 11/16/2025

Welcome to Module 4! During this module, we will be installing MySQL and PyCharm. We will also be digging into basic SQL commands.

### Deliverables
1) Module 4.1 Discussion Board Initial Post - Due by Thursday 11:59 p.m., CST.
2) Discussion Board Responses - Due by Sunday 11:59 p.m., CST.
3) Module 4.2 Assignment: MySQL - Due by Sunday 11:59 p.m., CST.
4) Optional: PyCharm & VSCode

### Discussion Board
**MySQL**

For this module's discussion board assignment respond to **one** the following topics:
1) Describe DDL. Provide at least two examples of DDL commands and explain when they might be used.
2) Describe DML. Provide at least two examples of DML commands and explain when they might be used.
3) Describe TCL. Provide at least two examples of TCL commands and explain when they might be used.
4) Describe DCL. Provide at least two examples of DCL commands and explain when they might be used.

### Assignments
#### Assignment 4.2
**Assignment: MySQL Install**

For this assignment, you will be installing MySQL. There are a couple of links above for guidance in installing MySQL on either a Windows machine, or a Mac machine. If you have issues, I strongly suggest you ask in this module's forum, or the cohort's discord site.

**Instructions**
1) Create (if you haven't already) a directory in CSD-310 named module-4.
2) Based on your computer's Operating System, select a link above to install MySQL. When following the install process, make sure you write down your root password. You'll be using it frequently!
3) Once MySQL has been installed, start the database through the terminal window. In Windows, the terminal window will show up in your list when you click on the 'Window' icon in the lower left part of your desktop, then MySQL. Once it opens, you'll be asked for your password.
    - Create a Word document and put your name and assignment number on the first page.Take a screenshot of your initial database connection, and paste it into the Word document.
    - Create a database..
        - The basic syntax for creating a database in MySQL is
        - CREATE DATABASE "database-name";
    - Create a database named movies.
    - MySQL: Show Databases
        - SHOW DATABASES;
    - Take a screenshot of the output from the show database command, and paste into the Word document. Save your document as "your-last-name"-"assignment-name".docx into your CSD-310/module-4 directory.
4) I want to see whether or not the database was created.

**Deliverables**

1) Combine the images into a single word document and include your name, date, and assignment on the first page.
2) Save your document as "your-last-name"-"assignment-name" .docx into your CSD-310/module-4 directory.

## Module 5
11/10/2025 - 11/16/2025

Welcome to Module 5! During this module, we will be taking a first look at SQL functions and creating an ERD for future exercises.

### Deliverables
1) Module 5.1 Discussion Board Initial Post - Due by Thursday 11:59 p.m., CST.
2) Discussion Board Responses - Due by Sunday 11:59 p.m., CST.
3) Module 5.2 Assignment: MySQL Functions- Due by Sunday 11:59 p.m., CST.
4) Module 5.3 Assignment: Movies Database ERD- Due by Sunday 11:59 p.m., CST.

### Discussion Board
**SQL**

For this module's discussion board assignment respond to **one** the following topics:
1) You run a query on the mysql.user table and find user accounts with the hostname listed as "%". What does this mean, and what concerns might that cause?
2) Would you create a user with a blank password? Why or why not?
3) What would be the reason for granting permissions to a user and then immediately revoking those permissions?
4) How often should users and their permissions be monitored? Why?

### Assignments
#### Assignment 5.2
**SQL Functions**

MySQL has many native functions that will come in handy from time to time. One is the current_date() function referenced in the previous chapter.

SELECT CURRENT_DATE(); will retrieve the current date in YYYY-MM-DD format, it also provides a column header of current_date(). Instead of having a column header as the function name, you can stipulate what alias you'd like to use. SELECT CURRENT_DATE() AS 'Today\'s Date'; will return the same result with a column header of Today's Date, which is much more user friendly. The \ is an escape character so you could use the apostrophe in the column header. If you have only a single word as an alias, you do not need to enclose it in single quotation marks.


**Instructions**
1) Create (if you haven't already) a directory in CSD-310 named module-5.
2) Create a Word document and put your name and assignment number on the first page.
3) Go out to the W3Schools links above, and select at least three functions to experiment with. For each:
    - Provide an explanation of when it might be used.
    - Provide an appropriate alias for the column header in the results.
    - Provide the SQL statment, run the statement, then take a screenshot of the results and paste it into your Word document. Save your document as "your-last-name"-"assignment-name".docx into your CSD-310/module-5 directory.

**Deliverables**
1) Combine the images into a single word document and include your name, date, and assignment on the first page..
2) Save your document as "your-last-name"-"assignment-name".docx into your CSD-310/module-5 directory.

## Module 6
11/17/2025 - 11/24/2025

Welcome to Module 6! During this module, creating the tables for the movies database and using a python script to access the MySQL database..

**Deliverables**
1) Module 6.1 Discussion Board Initial Post - Due by Thursday 11:59 p.m., CST.
2) Discussion Board Responses - Due by Sunday 11:59 p.m., CST.
3) Module 6.2 Assignment: Movies: Setup - Due by Sunday 11:59 p.m., CST.

### Discussion Board
For this module's discussion board assignment respond to **one** the following topics:
1) What is a primary key? Provide characteristics and an example for what type of field could be used, and what type of field should NOT be used as a primary key. Does each table need a primary key? Why or why not??
2) What is a foreign key? Provide an example for how a foreign key might be used. What are some of the issues associated with using foreign keys?
3) What are the three ways in which you can declare a comment in SQL? Provide an example of each and when it might be used.
4) What are two possible responses from the database if a user attempts to delete a record in a parent table for which there are associated records in a child table? How should each response be met?

### Assignment
#### Assignment 6.2
For this assignment, you will be learning how to create database tables, run SQL scripts from the terminal window to create tables, and how to connect a Python program to MySQL. Since these files are going to be pushed to GitHub in a public repository, we need to protect the login information. There is a lot of information to absorb in this assignment. Make sure you take your time to understand what you are doing and why you are doing it.

In this example, we are inserting a new record in the film table and mapping the values. The order you place the items in the VALUES section must match the order you have for the COLUMN VALUES. Remember, though, if the _id is auto-incremented, you do not include that in the VALUES list. Additionally, you'll see that to include the_id from studio and genre, I'm doing a SELECT to get the correct _id for for each type.

**Instructions**
1) Create (if you haven't already) a directory in CSD-310 named module-6.
2) Create a Word document and put your name and assignment number on the first page.
3) Start MySQL Command Line Client. The .sql script can only be run in the MySQL command line terminal.
    - Log in to command line provided by MySQL. Or... If you click on 'Terminal' in the bottom menu bar in PyCharm, you've got some choices. On my machine Windows Powershell opens up by default. If you'd rather use the Command Prompt, click on the down arrow next to the '+' sign and select Command Prompt. You can also add a terminal for MySQL by clicking that '+' sign, adding another Command Prompt and then changing the directory to the bin of your MySQL server, on my machine it is: cd program files\mysql\mysql server 8.0\bin You can then use the following the connect to the MySQL Interface mysql -u root -p where root is the username you want to use. The -p means you will be prompted for a password. Same options using VSCode.
4) Once logged into MySQL in the command line of your choice, move to the desired database.
    - use "database name";
    - USE movies;
5) Run the SQL script
    - source "path_to_the_ sql_script".sql;
    - Example: source d:/CSD/csd_310/db_init_2022.sql;
    - Note: the db_init_2022.sql script is attached to this assignment.
    - Take a screenshot of the last couple of lines you see once you've run the script. Copy into the Word document. Save your document as "your-last-name"-"assignment-name".docx into your CSD-310/module-6 directory.
6) Show a list of database tables (this assumes you have activated the database)
    - Move to database: use "database name"
    - USE movies;
    - Show tables
    - SHOW TABLES;
        - Take a screenshot of the result of SHOW TABLES. Copy into the Word document. Save your document as "your-last-name"-"assignment-name".docx into your CSD-310/module-6 directory.

7) MySQL: Python Connector
    - First, make sure you have the mysql-connector-python driver installed.
    - MySQL: Python Driver (pip) - run in generic (not MySQL) command line terminal
    - pip install mysql-connector-python
8) MySQL: Secure Login Info
    - In Python we can secure login info by using a package that gives us the ability to store these secret credentials in a hidden file (.env) which git ignores so the file can't be tracked. If you look in your .gitignore file on GitHub, you'll see a section: # Environments, which lists .env.
    - Two things to do here, first is to download the _.env Click for more options fIle and save into your Module 6 directory (when you save it, add a dot before the name.. should be saved as .env). Take a look at the file in a text editor. You'll see it has the values for USER, PASSWORD, HOST AND DATABASE. If you used different values than were in the db_init_2022 file, you'll need to make changes to that .env file
    - Second is to install the dotenv package: pip install python-dotenv
9) MySQL: mysql_test.py.
    - Python imports needed
    
```python
""" import statements """
import mysql.connector # to connect
from mysql.connector import errorcode

import dotenv # to use .env file
from dotenv import dotenv_values
```
- MySQL: mysql_test.py.Database config object; use YOUR user (could be root, or the user created in the db_init_2022.sql file) and associated password
```python
# using our .env file
secrets = dotenv_values(".env")

""" database config object """
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True #not in .env file
}
```
- MySQL: mysql_test.py. Connection test code
```python
try:
    """ try/catch block for handling potential MySQL database errors """

    db = mysql.connector.connect(**config) # connect to the movies database 
    
    # output the connection status 
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...")

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
```

- Save your mysql_test.py file into your module-6 directory.
- Run the script and take a screenshot of the results and paste into the Word document. Save your document as "your-last-name",docx into your CSD-310/module-6 directory.

**Deliverables**
1) Combine the images and your link to the GitHub repository into a single word document and include your name, date, and assignment on the first page.
2) Save your document as "your-last-name"-"assignment-name' .docx into your CSD-310/module-6 directory.
3) mysql_test.py
4) Zip up files or submit separately.
