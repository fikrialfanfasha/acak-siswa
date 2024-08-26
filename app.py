from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

siswa = [
    ("ANISA EKA MEILESTARI", 'P'), ("AYU WULAN DARI", 'P'), ("CELSI MUSTIKAWATI", 'P'),
    ("DADAN RIANTO", 'L'), ("FEBRIANSYAH", 'L'), ("FIKI AGUSTIAN", 'L'),
    ("FIKRI AHMAD ZAKIA", 'L'), ("GALIH RIZHAN FAUZAN", 'L'),
    ("INDAH AYU FITRI NURAENI MUHAPILAH", 'P'), ("INE NURUNIAH", 'P'),
    ("KAILA MELANI", 'P'), ("KHANZA SIYAMUL FADILLAH", 'P'),
    ("LINGGA NINDI ALIFA", 'P'), ("LIVIA SHINTIA", 'P'), ("NURSACI HAFITRIANI", 'P'),
    ("RAMA RAMDANI", 'L'), ("SYVA AULIYAH", 'P'), ("AMELIA REGISTA AGUSTIN", 'P'),
    ("ANGGI NURHIDAYAH", 'P'), ("DELLA SAFIRA UTAMI", 'P'),
    ("DEQI MUHAMMAD DZUL FACHRY", 'L'), ("FAZWA REINIFA RAMADHANI", 'P'),
    ("FENI NURAGISTIN", 'P'), ("GALIH ARAHMAN", 'L'), ("JIHAN FAHIRA", 'P'),
    ("LINDA APRILIA", 'P'), ("LYLA SENJA ASHARY", 'P'), ("MARSHA SEPTIANI", 'P'),
    ("MUHAMAD TASDIK", 'L'), ("NENG YUNI LESTARI", 'P'), ("SEYPA BABAN IBRAHIM", 'L'),
    ("WULAN ZESIKA SARI", 'P'), ("ADI MAULANA FIRMANSAH", 'L'),
    ("AFDAL AHMAD HIDAYAT", 'L'), ("ALFI MUBAROK", 'L'), ("NIDA RACHMA TAZKIA", 'P')
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/daftar-siswa')
def daftar_siswa():
    return jsonify([{'nama': nama, 'gender': gender} for nama, gender in siswa])

@app.route('/buat-kelompok', methods=['POST'])
def buat_kelompok():
    random.shuffle(siswa)

    kelompok = [[] for _ in range(6)]

    for i, siswa_data in enumerate(siswa):
        kelompok[i % 6].append({'nama': siswa_data[0], 'gender': siswa_data[1]})

    response_data = [{'kelompok': i+1, 'anggota': kelompok[i]} for i in range(6)]
    
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
