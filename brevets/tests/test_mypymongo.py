"""
Nose tests for mypymongo.py

Write your tests HERE AND ONLY HERE.
"""
from mypymongo import brevet_insert, brevet_find
import arrow
import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

def test_1():
    start_time = '2021-01-01T00:00'
    brevet_dist_km = 200
    items = [
    {"miles": 0.000000, "km": 0, "location": 'location1', "open_time": start_time, "close_time": '2021-01-01T01:00'},
    {"miles": 31.068550, "km": 50, "location": 'location2', "open_time": '2021-01-01T01:28', "close_time": '2021-01-01T03:30'},
    {"miles": 62.137100, "km": 100, "location": 'location3', "open_time": '2021-01-01T02:56', "close_time": '2021-01-01T06:40'},
    {"miles": 93.205650, "km": 150, "location": 'location4', "open_time": '2021-01-01T04:25', "close_time": '2021-01-01T10:00'},
    {"miles": 124.274200, "km": 200, "location": 'location5', "open_time": '2021-01-01T05:53', "close_time": '2021-01-01T13:30'},
    ]

    test_insert = brevet_insert(start_time, brevet_dist_km, items)
    assert test_insert != None

def test_2():
    start_time = '2021-01-01T00:00'
    brevet_dist_km = 200
    items = [
    {"miles": 0.000000, "km": 0, "location": 'location1', "open_time": start_time, "close_time": '2021-01-01T01:00'},
    {"miles": 31.068550, "km": 50, "location": 'location2', "open_time": '2021-01-01T01:28', "close_time": '2021-01-01T03:30'},
    {"miles": 62.137100, "km": 100, "location": 'location3', "open_time": '2021-01-01T02:56', "close_time": '2021-01-01T06:40'},
    {"miles": 93.205650, "km": 150, "location": 'location4', "open_time": '2021-01-01T04:25', "close_time": '2021-01-01T10:00'},
    {"miles": 124.274200, "km": 200, "location": 'location5', "open_time": '2021-01-01T05:53', "close_time": '2021-01-01T13:30'},
    ]

    test_insert = brevet_insert(start_time, brevet_dist_km, items)
    fetch_holder = brevet_fetch()
    fetch_check = brevet_fetch(start_time, brevet_dist_km, items)
    assert fetch_check == fetch_holder