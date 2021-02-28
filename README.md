<img src="https://miro.medium.com/max/700/1*xlRpJixAInrMlIhn5KINgA.jpeg" width="25%" align="right" alt="" title="Cassandra logo" />

### Udacity Data Engineering Nanodegree
# Project 2: Data Modeling with Cassandra

 

## Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.

They'd like a data engineer to create an Apache Cassandra database which can create queries on song play data. This will inform future projects that improve the Sparkify music service.

Your role is to create a database for this analysis. You'll be able to test your database by running queries given to you by the analytics team at Sparkify.


##### &nbsp;

## Goals
In this project, we apply what we've learned on data modeling with Apache Cassandra to build an ETL pipeline using Python.

To complete the project, you need to:
1. Model your data by creating tables in Apache Cassandra to run queries
2. Write an ETL pipeline that transfers data from a set of CSV files and inserts it into Apache Cassandra tables.


##### &nbsp;

## Project Setup & Instructions

##### &nbsp;

### Datasets
For this project, you'll be working with one dataset: event_data. The directory of CSV files partitioned by date. Here are examples of filepaths to two files in the dataset:
```
event_data/2018-11-08-events.csv
event_data/2018-11-09-events.csv
```

##### &nbsp;

### Project Template
To get started with the project, go to the workspace on the next page, where you'll find the project template (a Jupyter notebook file). You can work on your project and submit your work through this workspace.

The project template includes one Jupyter Notebook file, in which:

- you will process the `new_event_data.csv` dataset to create a denormalized dataset
- you will model the data tables keeping in mind the queries you need to run
- you have been provided queries that you will need to model your data tables for
- you will load the data into tables you create in Apache Cassandra and run your queries

##### &nbsp;

### Project Steps
Below are steps you can follow to complete each component of this project.

#### Modeling your NoSQL database or Apache Cassandra database
1. Design tables to answer the queries outlined in the project template
1. Write Apache Cassandra `CREATE KEYSPACE` and `SET KEYSPACE` statements
1. Develop your CREATE statement for each of the tables to address each question
1. Load the data with `INSERT` statement for each of the tables
1. Include `IF NOT EXISTS` clauses in your `CREATE` statements to create tables only if the tables do not already exist. We recommend you also include `DROP TABLE` statement for each table, this way you can run drop and create tables whenever you want to reset your database and test your ETL pipeline
1. Test by running the proper select statements with the correct `WHERE` clause

#### Build ETL Pipeline
1. Implement the logic in section Part I of the notebook template to iterate through each event file in `event_data` to process and create a new CSV file in Python
1. Make necessary edits to Part II of the notebook template to include Apache Cassandra `CREATE` and `INSERT` statements to load processed records into relevant tables in your data model
1. Test by running `SELECT` statements after running the queries on your database

##### &nbsp;

## My Implementation

You can step through my implementation of the Cassandra database and ETL pipeline [here in this notebook](notebook/data_modeling_with_cassandra.ipynb) or you can follow simple python implemention

##### &nbsp;

#### Result of this modeling:
```python
*********Result - 1 *************
Row(artist_name='Faithless', song_title='Music Matters (Mark Knight Dub)', song_length=495.30731201171875)

*************** Result - 2 *******************
Row(artist_name='Down To The Bone', song_name="Keep On Keepin' On", first_name='Sylvie', last_name='Cruz')
Row(artist_name='Three Drives', song_name='Greece 2000', first_name='Sylvie', last_name='Cruz')
Row(artist_name='Sebastien Tellier', song_name='Kilometer', first_name='Sylvie', last_name='Cruz')
Row(artist_name='Lonnie Gordon', song_name='Catch You Baby (Steve Pitron & Max Sanna Radio Edit)', first_name='Sylvie', last_name='Cruz')

*************** Result - 3 ********************
Row(artist_name='The Black Keys', song_title='All Hands Against His Own', song_length=196.9105682373047, first_name='Tegan', last_name='Levine')
```