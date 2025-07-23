from flask import Flask, jsonify, render_template, request
import random
import json

app = Flask(__name__)

def load_siswa():
    with open('siswa.json', 'r') as file:
        return json.load(file)

siswa = load_siswa()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/daftar-siswa')
def daftar_siswa():
    return jsonify(siswa)

@app.route('/buat-kelompok', methods=['POST'])
def buat_kelompok():
    jumlah_kelompok = 6
    kelompok = [[] for _ in range(jumlah_kelompok)]
    gender_count = [{'L': 0, 'P': 0} for _ in range(jumlah_kelompok)]

    # Acak siswa tanpa memisahkan gender
    siswa_acak = siswa[:]
    random.shuffle(siswa_acak)

    for s in siswa_acak:
        # Cari kelompok dengan gender seimbang
        kandidat = sorted(
            range(jumlah_kelompok),
            key=lambda i: (gender_count[i][s['gender']], len(kelompok[i]))
        )
        index = kandidat[0]
        kelompok[index].append(s)
        gender_count[index][s['gender']] += 1

    response_data = [{'kelompok': i + 1, 'anggota': kelompok[i]} for i in range(jumlah_kelompok)]
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
