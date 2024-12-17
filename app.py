import streamlit as st

# Pilihan Navigasi
st.sidebar.title("To Do List")
page = st.sidebar.radio("Catatan", ["Read", "Create", "Update", "Delete"])

if page == "Read":
    from noted.read import main as read
    read()  # Jalankan fungsi utama dari read.py

elif page == "Create":
    from noted.create import main as create
    create()  # Jalankan fungsi utama dari upda.py

elif page == "Update":
    from noted.update import main as update
    update()  # Jalankan fungsi utama dari update.py

elif page == "Delete":
    from noted.delete import main as delete
    delete()  # Jalankan fungsi utama dari delete.py
