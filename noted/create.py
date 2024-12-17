import streamlit as st

def main():
    st.title("Tambah Data Catatan")
    # Form input untuk data
    judul = st.text_input("Judul")
    deskripsi = st.text_area("Deskripsi")
    batas_waktu = st.date_input("Batas Waktu")

    # Tombol untuk menyimpan data
    if st.button("Simpan"):
        if judul and deskripsi and batas_waktu:
            try:
                # Membuat koneksi ke database
                from koneksi  import create_connection
                konek = create_connection()
                cursor = konek.cursor()

                # Query untuk menambahkan data
                query = "INSERT INTO noted (judul, deskripsi, batas_waktu) VALUES (%s, %s, %s)"
                data = (judul, deskripsi, batas_waktu)
                cursor.execute(query, data)
                konek.commit()

                # Notifikasi berhasil
                st.success("Data berhasil disimpan!")
                konek.close()
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")
        else:
            st.warning("Harap lengkapi semua data!")

