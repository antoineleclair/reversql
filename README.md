ReverSQL
========

This is a simple script to take all the `CREATE TABLE` and `CREATE SEQUENCE` from a SQL file and output the corresponding `DROP` in reverse. I wrote this when dealing with Play Framework 2.0 evolutions (migrations) and Oracle database. I use it to generate the `down` evolution from a `up` evolution.
