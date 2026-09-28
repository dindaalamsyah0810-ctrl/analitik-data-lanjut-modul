import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Judul aplikasi
st.title("Streamlit Simple App")


# Menambahkan navigasi di sidebar
page = st.sidebar.radio(
    "Pilih halaman",
    ["Dataset", "Visualisasi"],
    key="page_navigation"
)


# =========================
# HALAMAN DATASET
# =========================
if page == "Dataset":
    st.header("Halaman Dataset")

    # Baca file CSV
    data = pd.read_csv("pddikti_example.csv")

    # Tampilkan data di Streamlit
    st.write(data)


# =========================
# HALAMAN VISUALISASI
# =========================
elif page == "Visualisasi":
    st.header("Halaman Visualisasi")

    # Baca file CSV
    data = pd.read_csv("pddikti_example.csv")

    # Filter berdasarkan universitas
    selected_university = st.selectbox(
        "Pilih Universitas",
        data["universitas"].unique()
    )

    filtered_data = data[
        data["universitas"] == selected_university
    ]

    # Buat visualisasi
    plt.figure(figsize=(12, 6))

    for prog_studi in filtered_data["program_studi"].unique():

        subset = filtered_data[
            filtered_data["program_studi"] == prog_studi
        ]

        # Urutkan data berdasarkan ID secara menurun
        subset = subset.sort_values(
            by="id",
            ascending=False
        )

        # Buat garis untuk setiap program studi
        plt.plot(
            subset["semester"],
            subset["jumlah"],
            label=prog_studi
        )

    # Pengaturan grafik
    plt.title(
        f"Visualisasi Data untuk {selected_university}"
    )

    plt.xlabel("Semester")
    plt.ylabel("Jumlah")

    plt.xticks(rotation=90)

    plt.legend()

    # Tampilkan grafik di Streamlit
    st.pyplot(plt)