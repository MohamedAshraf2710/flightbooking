# database.py

import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "flights.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_table():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS reservations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                flight_number TEXT,
                departure TEXT,
                destination TEXT,
                date TEXT,
                seat_number TEXT
            )
        ''')
        conn.commit()


def insert(name, flight_number, departure, destination, date, seat_number):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, flight_number, departure, destination, date, seat_number))
        conn.commit()


def view():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM reservations")
        return cur.fetchall()


def update(id, name, flight_number, departure, destination, date, seat_number):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute('''
            UPDATE reservations
            SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=?
            WHERE id=?
        ''', (name, flight_number, departure, destination, date, seat_number, id))
        conn.commit()


def delete(id):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM reservations WHERE id=?", (id,))
        conn.commit()