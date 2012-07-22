ReverSQL
========

This is a simple script to take all the `CREATE TABLE` and `CREATE SEQUENCE` from a SQL file and output the corresponding `DROP` in reverse. I wrote this when dealing with Play Framework 2.0 evolutions (migrations) and Oracle database. I use it to generate the `down` evolution from a `up` evolution.

Usage
-----

    ./reversql.py filename.sql
    
Example
-------

It will take a file like this:

```sql
CREATE TABLE programs (
    id NUMBER PRIMARY KEY,
    title VARCHAR(255) NOT NULL
);

CREATE SEQUENCE programs_id_seq
    START WITH 1 
    INCREMENT BY 1 
    NOMAXVALUE;
    
CREATE TABLE donors (
    id NUMBER PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE SEQUENCE donors_id_seq
    START WITH 1
    INCREMENT BY 1
    NOMAXVALUE;
    
CREATE TABLE contacts (
    id NUMBER PRIMARY KEY,
    name VARCHAR(255) NOT NULL
    CONSTRAINT fk_contacts_donor_id
        FOREIGN KEY (donor_id) REFERENCES donors(id)
);

CREATE SEQUENCE contacts_id_seq
    START WITH 1
    INCREMENT BY 1
    NOMAXVALUE;
```

And it will output this:

```sql
DROP SEQUENCE contacts_id_seq;
DROP TABLE contacts;
DROP SEQUENCE donors_id_seq;
DROP TABLE donors;
DROP SEQUENCE programs_id_seq;
DROP TABLE programs;
```
