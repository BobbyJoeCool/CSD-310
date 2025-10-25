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
