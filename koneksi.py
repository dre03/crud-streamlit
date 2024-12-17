import mysql.connector

# Konfigurasi koneksi ke database
def create_connection():
    connection = mysql.connector.connect(
        host="localhost",        # Host Laragon (default: localhost)
        user="root",             # Username MySQL default di Laragon
        password="",             # Password MySQL (default kosong di Laragon)
        database="todolist" # Ganti dengan nama database Anda
    )
    return connection