import streamlit as st
import koneksi as kon
import pandas as pd

def main():
    st.title("Hapus Data Catatan")

    # Membuat koneksi ke database
    konek = kon.create_connection()

    # Query untuk mengambil semua data
    query = "SELECT id, judul, deskripsi, batas_waktu FROM noted"
    data = pd.read_sql(query, konek)

    # Jika data tersedia, tampilkan pilihan
    if not data.empty:
        # Dropdown untuk memilih data berdasarkan ID
        id_pilih = st.selectbox("Pilih ID untuk dihapus", data['id'])

        # Menampilkan data yang dipilih
        data_terpilih = data[data['id'] == id_pilih]
        st.write("Data yang akan dihapus:")
        st.write(f"Judul: {data_terpilih.iloc[0]['judul']}")
        st.write(f"Deskripsi: {data_terpilih.iloc[0]['deskripsi']}")
        st.write(f"Batas Waktu: {data_terpilih.iloc[0]['batas_waktu']}")

        # Tombol untuk konfirmasi penghapusan
        if st.button("Hapus"):
            try:
                cursor = konek.cursor()

                # Query untuk menghapus data
                delete_query = "DELETE FROM noted WHERE id = %s"
                cursor.execute(delete_query, (id_pilih,))
                konek.commit()

                st.success("Data berhasil dihapus!")
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")
            finally:
                konek.close()
    else:
        st.warning("Tidak ada data untuk dihapus.")
