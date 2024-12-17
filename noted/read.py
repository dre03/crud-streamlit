import streamlit as st
import koneksi as kon
import pandas as pd

# Fungsi utama Streamlit
def main():
    st.title("Menampilkan data Catatan")

    # Membuat koneksi
    konek = kon.create_connection()

    # Query untuk mengambil data
    query = "SELECT judul, deskripsi, batas_waktu FROM noted"  # Ganti dengan nama tabel Anda
    data = pd.read_sql(query, konek)

    # Menampilkan Data
    st.subheader("Data Catatan")
    st.table(data) # Tampilakandata dengan tabel

      # Menutup koneksi database
    konek.close()

# if __name__ == "__main__":
#     main()
