import streamlit as st
import koneksi as kon
import pandas as pd

def main():
    st.title("Update Data Catatan")

    # Membuat koneksi ke database
    konek = kon.create_connection()

    # Query untuk mengambil semua data
    query = "SELECT id, judul, deskripsi, batas_waktu FROM noted"
    data = pd.read_sql(query, konek)

    # Jika data tersedia, tampilkan pilihan
    if not data.empty:
        # Dropdown untuk memilih data berdasarkan ID
        id_pilih = st.selectbox("Pilih ID untuk diupdate", data['id'])

        # Menampilkan data lama dari ID terpilih
        data_terpilih = data[data['id'] == id_pilih]
        judul_lama = data_terpilih.iloc[0]['judul']
        deskripsi_lama = data_terpilih.iloc[0]['deskripsi']
        batas_waktu_lama = data_terpilih.iloc[0]['batas_waktu']

        # Form input untuk data baru
        judul_baru = st.text_input("Judul Baru", value=judul_lama)
        deskripsi_baru = st.text_area("Deskripsi Baru", value=deskripsi_lama)
        batas_waktu_baru = st.date_input("Batas Waktu Baru", value=pd.to_datetime(batas_waktu_lama))

        # Tombol untuk menyimpan perubahan
        if st.button("Update"):
            if judul_baru and deskripsi_baru and batas_waktu_baru:
                try:
                    cursor = konek.cursor()

                    # Query untuk mengupdate data
                    update_query = """
                    UPDATE noted
                    SET judul = %s, deskripsi = %s, batas_waktu = %s
                    WHERE id = %s
                    """
                    cursor.execute(update_query, (judul_baru, deskripsi_baru, batas_waktu_baru, id_pilih))
                    konek.commit()

                    st.success("Data berhasil diupdate!")
                except Exception as e:
                    st.error(f"Terjadi kesalahan: {e}")
                finally:
                    konek.close()
            else:
                st.warning("Harap lengkapi semua data!")
    else:
        st.warning("Tidak ada data untuk diupdate.")
