import os
from groq import Groq  # Import Groq API
from agents import Agents  # Pastikan modul Agents yang telah Anda buat tetap digunakan
from dotenv import load_dotenv

load_dotenv()

class Tasks:
    def __init__(self, input_data):
        self.input_data = input_data
        self.agent = Agents().Adviser()  # Mengambil agent dari Agents class

    def GivingAdvise(self):
        # Deskripsi tugas yang mendetail, sama seperti pada kodingan `crewai`
        task_description = f"""
            Analisa hasil jawaban questioner minat berikut: {self.input_data}.
            Prediksi minat siswa dan berikan insight mendalam sebagai seorang expert di bidang IT untuk membantu siswa yang baru mengenal IT mengembangkan minatnya.

            1. Analisis Minat: Berdasarkan hasil jawaban siswa, identifikasi minat dominan mereka di salah satu bidang IT berikut:
            - Front End Development: Desain antarmuka dan pengalaman pengguna.
            - Back End Development: Sistem backend, logika bisnis, dan manajemen database.
            - Full Stack Development: Keterampilan kombinasi dalam pengembangan aplikasi secara menyeluruh.
            - Game Development: Pengembangan mekanisme permainan dan pengalaman interaktif.

            2. Rekomendasi Pengembangan: Berikan strategi yang terfokus untuk mengembangkan minat yang teridentifikasi. Ini dapat mencakup:
            - Sumber Belajar: Rekomendasi kursus atau materi yang relevan (misalnya, platform seperti freeCodeCamp, Codecademy, atau Coursera).
            - Keterampilan Utama: Daftar teknologi dan keterampilan yang harus dipelajari untuk setiap bidang (misalnya, HTML/CSS untuk Front End, Node.js untuk Back End, Unity/Unreal untuk Game Development).
            - Proyek Awal: Saran proyek pemula yang dapat meningkatkan pemahaman mereka (misalnya, membangun halaman web statis, API sederhana, atau game 2D sederhana).

            3. Insight Expert: Wawasan mendalam sebagai seorang expert di bidang IT, termasuk saran mengenai tren terbaru di industri (misalnya, "Tren saat ini menunjukkan permintaan tinggi untuk pengembang Full Stack dengan keterampilan di DevOps dan pengembangan cloud"). Sertakan tips tentang bagaimana siswa bisa merencanakan perjalanan karir mereka di IT berdasarkan minat yang diidentifikasi.

            4. Langkah Selanjutnya: Berikan panduan praktis untuk langkah-langkah pembelajaran selanjutnya, termasuk bagaimana siswa dapat melibatkan diri dalam komunitas IT (misalnya, forum diskusi, hackathon, atau project collaboration platform seperti GitHub).
        """

        # Menghubungkan dengan Groq API untuk menyelesaikan task
        try:
            client = Groq(api_key=os.getenv("GROQ_API_KEY"))
            response = client.chat.completions.create(
                model="llama3-8b-8192",  # Model yang digunakan
                messages=[
                    {"role": "system", "content": self.agent["description"]},  # Menggunakan deskripsi agent yang sama
                    {"role": "user", "content": task_description}  # Mengirim prompt yang sudah dirancang
                ],
                max_tokens=1000  # Batas maksimum token untuk memastikan jawaban lebih lengkap
            )
            return response.choices[0].message.content  # Mengembalikan hasil dari API
        except Exception as e:
            return f"Terjadi kesalahan: {str(e)}"

# Penggunaan
if __name__ == "__main__":
    task = Tasks("Jawaban siswa dari questioner mengenai minat di IT.")
    hasil = task.GivingAdvise()
    print(hasil)
