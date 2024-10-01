import os
import streamlit as st
import matplotlib.pyplot as plt
from task import Tasks

# **Masukkan API Key Anda di sini**
os.environ["GROQ_API_KEY"] = "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"  # Gantilah dengan API Key Groq Anda

# Judul aplikasi
st.title("Asesmen Minat Siswa: Front End, Back End, Full Stack, atau Game Development")

# Inputan untuk nomor absen, nama, dan kelas
st.header("Informasi Siswa")
nama = st.text_input("Nama:")
nomor_absen = st.number_input("Nomor Absen:", min_value=1, step=1)
kelas = st.selectbox("Kelas:", ["X RPL A", "X RPL B", "X RPL C"])

# Data minat awal
data_minat = {
    "Front End": 0,
    "Back End": 0,
    "Full Stack": 0,
    "Game Development": 0
}

# Fungsi untuk menambahkan nilai ke data minat
def update_minat(pilihan):
    if "a)" in pilihan:
        data_minat["Front End"] += 1
    elif "b)" in pilihan:
        data_minat["Back End"] += 1
    elif "c)" in pilihan:
        data_minat["Full Stack"] += 1
    elif "d)" in pilihan:
        data_minat["Game Development"] += 1

# Pertanyaan dan opsi jawaban
pertanyaan = [
    "1. Mana dari berikut ini yang paling menarik perhatian Anda?",
    "2. Apa yang paling membuat Anda puas saat menyelesaikan sebuah proyek?",
    "3. Ketika menghadapi masalah dalam pemrograman, apa yang lebih sering Anda pikirkan?",
    "4. Mana dari berikut ini yang lebih Anda nikmati?",
    "5. Keterampilan apa yang ingin Anda tingkatkan lebih jauh?",
    "6. Apa yang paling Anda perhatikan saat menggunakan aplikasi atau game?",
    "7. Jika Anda harus memilih, mana yang lebih Anda sukai?",
    "8. Apa jenis proyek yang ingin Anda kerjakan dalam waktu dekat?",
    "9. Apa yang menurut Anda lebih menarik dari teknologi berikut?",
    "10. Di mana Anda melihat diri Anda lima tahun dari sekarang?"
]

opsi_jawaban = [
    ("a) Membuat tampilan halaman web yang menarik secara visual", 
     "b) Merancang logika dan struktur data di balik aplikasi", 
     "c) Menggabungkan keterampilan dalam membangun tampilan dan logika aplikasi", 
     "d) Membangun dunia dan pengalaman interaktif dalam game"),

    ("a) Ketika tampilan web atau aplikasi terlihat indah dan fungsional", 
     "b) Saat aplikasi berjalan lancar dan semua data diproses dengan benar", 
     "c) Ketika bisa membangun aplikasi lengkap, dari tampilan hingga logika yang kompleks", 
     "d) Ketika karakter atau mekanisme dalam game berfungsi sesuai harapan"),

    ("a) Bagaimana cara membuat tampilan lebih user-friendly dan responsif", 
     "b) Bagaimana cara membuat algoritma yang efisien dan mengoptimalkan backend", 
     "c) Bagaimana menghubungkan antara tampilan dan logika program dengan baik", 
     "d) Bagaimana membuat mekanisme permainan yang seru dan interaktif"),

    ("a) Mengutak-atik desain, warna, dan layout untuk membuat tampilan web lebih menarik", 
     "b) Menulis kode yang efisien untuk memproses data dan melakukan perhitungan", 
     "c) Membangun aplikasi dari awal hingga akhir, baik frontend maupun backend", 
     "d) Merancang karakter, latar belakang, atau skenario dalam game"),

    ("a) Penguasaan HTML, CSS, JavaScript, dan framework seperti React atau Vue.js", 
     "b) Pemahaman mendalam tentang bahasa backend seperti Python, PHP, atau Node.js", 
     "c) Menjadi mahir di kedua area, baik frontend maupun backend", 
     "d) Memahami lebih dalam mekanika permainan dan pengembangan game menggunakan Unity atau Unreal Engine"),

    ("a) Apakah tampilan aplikasinya menarik dan mudah digunakan", 
     "b) Bagaimana performa dan kecepatan proses aplikasi", 
     "c) Apakah aplikasi tersebut berfungsi dengan baik secara keseluruhan, dari desain hingga fungsionalitas", 
     "d) Apakah gameplay-nya seru dan mekaniknya menantang"),

    ("a) Bekerja sama dengan tim desain untuk mempercantik tampilan aplikasi", 
     "b) Bekerja di belakang layar, mengoptimalkan kinerja dan keamanan aplikasi", 
     "c) Mengambil tanggung jawab penuh, dari awal hingga akhir pengembangan aplikasi", 
     "d) Berkolaborasi dengan tim kreatif untuk menciptakan game yang menyenangkan"),

    ("a) Merancang dan mengembangkan antarmuka pengguna (UI) untuk sebuah aplikasi", 
     "b) Membangun API dan sistem yang dapat mengelola data secara efisien", 
     "c) Membangun aplikasi web lengkap yang bisa diakses dan diandalkan", 
     "d) Mengembangkan game 2D atau 3D yang seru dan menarik"),

    ("a) Teknologi seperti CSS Grid, Flexbox, dan animasi CSS", 
     "b) Teknologi seperti server, database, dan RESTful API", 
     "c) Kedua teknologi di atas dan bagaimana mereka saling terhubung", 
     "d) Teknologi seperti game engine, animasi karakter, dan desain level"),

    ("a) Sebagai desainer atau pengembang front-end yang ahli dalam membuat antarmuka pengguna", 
     "b) Sebagai insinyur backend yang ahli dalam membangun sistem yang efisien dan aman", 
     "c) Sebagai pengembang full-stack yang mampu menangani semua aspek pengembangan aplikasi", 
     "d) Sebagai pengembang game profesional yang berkontribusi dalam pembuatan game terkenal")
]

# Menampilkan pertanyaan-pertanyaan
st.header("Pertanyaan Minat")
for i in range(len(pertanyaan)):
    st.write(pertanyaan[i])
    pilihan = st.radio("Pilih salah satu:", opsi_jawaban[i], key=i)
    update_minat(pilihan)

# Fungsi untuk memanggil agen dan tugas
def get_rekomendasi_agent(data_minat, nama, kelas, nomor_absen):
    input_data = f"Minat siswa: {data_minat}, Nama: {nama}, Kelas: {kelas}, Nomor Absen: {nomor_absen}"
    task_instance = Tasks(input_data)
    rekomendasi = task_instance.GivingAdvise()
    return rekomendasi


# Fungsi untuk menampilkan diagram lingkaran
def tampilkan_diagram_lingkaran(data):
    fig, ax = plt.subplots()
    labels = list(data.keys())
    sizes = list(data.values())
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    
    st.pyplot(fig)

    # Tombol untuk menampilkan hasil
if st.button("Tampilkan Hasil"):
    st.subheader("Diagram Minat Siswa")
    # Menampilkan diagram lingkaran (pie chart)
    tampilkan_diagram_lingkaran(data_minat)

    # Mendapatkan rekomendasi karir dari agen
    rekomendasi = get_rekomendasi_agent(data_minat, nama, kelas, nomor_absen)
    
    if rekomendasi:
        st.subheader("Rekomendasi Karir")
        st.markdown(rekomendasi)
