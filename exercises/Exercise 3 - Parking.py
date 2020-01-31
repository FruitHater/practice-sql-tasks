"""
Author: RedFantom
License: MIT License
Copyright (C) 2018 RedFantom
"""
from datetime import datetime
from database import open_database, execute_query


"""Open database"""
connection = open_database("parking.db")
fmt = "%d-%m-%Y"


"""Determine name of the owner of the car that is parked the longest"""
query1 = """SELECT ..."""
customer, = execute_query(connection, query1)[0]


"""Determine car type and how long for the customer of the last query"""
query2 = """SELECT ...""".format(customer)
start, end, car_type, spot_id = execute_query(connection, query2)[0]
duration = (datetime.strptime(end, fmt) - datetime.strptime(start, fmt)).days
print("{} owns a {} and it is staying for {} days in spot {}.".format(customer, car_type, duration, spot_id))
