"""
Author: RedFantom
License: MIT License
Copyright (C) 2018 RedFantom
"""
import pandas as pd
from database import open_database, print_dataframe, execute_query

connection = open_database("chinook.db")

"""Database Inspection"""
query1 = """SELECT name "Name" FROM sqlite_master WHERE type = 'table';"""
tables = pd.read_sql_query(query1, connection)
print_dataframe("Tables", tables)

"""List all media types"""
query2 = """SELECT ..."""
media_types = pd.read_sql_query(query2, connection)
print_dataframe("Media Types", media_types)

"""Count all tracks with each media type"""
for media_type in media_types["Type"]:
query3 = """SELECT ..."""
result = execute_query(connection, query3)
print()

"""Display amount of tracks and name for playlists"""
query4 = """SELECT ..."""
playlists = execute_query(connection, query4)
for playlist in playlists:
    print("Playlist {} with {} items costs €{:.2f}".format(*playlist))
print()

"""Determine average amount of items per invoice"""
query5 = """SELECT ..."""
result, = execute_query(connection, query5)[0]
print("Average number of items per invoice: {:.02f}".format(result))

"""Determine the maximum amount of items on a single invoice"""
query6 = """SELECT ..."""
result, = execute_query(connection, query6)[0]
print("Maximum amount of items on a single invoice:", result)

"""Determine the Employee with the customer who bought the most items"""
query7 = """SELECT ..."""
first_name, last_name = execute_query(connection, query7)[0]
print("{} {} is the most successful employee!".format(first_name, last_name))

"""Determine the most successful artist - most tracks"""
query8 = """SELECT ..."""
number, name = execute_query(connection, query8)[0]
print("Artist {} has the most songs with {} tracks.".format(name, number))


"""Determine the most successful artist - most sales"""
query9 = """SELECT ..."""
number, name = execute_query(connection, query9)[0]
print("Artist {} has the most sales with {} sales".format(name, number))

