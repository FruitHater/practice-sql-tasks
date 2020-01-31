"""
Author: RedFantom
License: MIT License
Copyright (C) 2018 RedFantom
"""
from database import open_database, execute_query


"""Open the Database"""
connection = open_database("northwind.db")


"""List all tables"""
query1 = """SELECT name FROM sqlite_master WHERE type='table';"""
tables = execute_query(connection, query1)
for table, in tables:
    print(table, end=", ")
print()


"""Find the category with the most products"""
query2 = """SELECT ..."""
_, name, description = execute_query(connection, query2)[0]
print("The largest category is {} containing {}.".format(name, description))


"""Find the Category with the most customers"""
query3 = """SELECT ..."""
n, country = execute_query(connection, query3)[0]
print("The country with the most customers is {} with {} customers.".format(country, n))


"""Find the most popular shipping method"""
query4 = """SELECT ..."""
_, company = execute_query(connection, query4)[0]
print("The most popular shipping company is {}.".format(company))


"""Determine the customer who ordered the biggest order"""
query5 = """SELECT ..."""
result, = execute_query(connection, query5)[0]
print("{} made the order with most items.".format(result))
