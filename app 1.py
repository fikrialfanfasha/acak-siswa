from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

siswa = [
    ("AFDA AZIZA", 'P'), ("ELSA RAMADHANI PUTRI", 'P'), ("GINA HIMALATUL ALIYA", 'P'),
    ("MEGA SITI FADILLAH", 'P'), ("NASYA NURTATIA ALYUZA", 'P'), ("NUR AISA SUPIANINGSIH", 'P'),
    ("RAHMANIA RAINA SONDARA", 'P'), ("REVAL PRIA PRATAMA", 'L'), ("RIKA AMELIA", 'P'),
    ("RIMA NURMADIANA", 'P'), ("SITI NUR LELA", 'P'), ("SILVIA ROSALINA", 'P'),
    ("AIA RIDA AYUNISA", 'P'), ("AIRIN AGUSTIN", 'P'), ("APRILLIA PRASTIKA DEVI", 'P'),
    ("ARBI PANDRI", 'L'), ("DERA TRI ANANDA", 'P'), ("DEVIA SYARIFATUN NURFITRIANI", 'P'),
    ("IMAS", 'P'), ("KARINA TRI UTAMI", 'P'), ("NABILA HAMZA", 'P'),
    ("SILVIA ALFADILAH", 'P'), ("AYU ROSDIYANI", 'P'), ("CHICA ANNISA SALSABILLA", 'P'),
    ("ENJEL AMELIA PUTRI", 'P'), ("GITA NURHASANAH", 'P'), ("KEIZYA TRIOKTAVIANY", 'P'),
    ("LAILA KHOIRUNISA", 'P'), ("NAZWA RAISYA LISDIAWATI SUHARTO", 'P'), ("NOVAL TRI CAHYA KURNIA", 'L'),
    ("PEBI DEWI AGUSTIN", 'P'), ("RAINIS INDRIYANTI KAMINOV", 'P'), ("WAWAY RAHMAWATI", 'P'),
    ("YUSI FAUZIAH NUREFENDI", 'P'), ("FAQRIS NIRWANSYAH PRAYOGA", 'L'), ("NADILA ALFIDA WIDIAWATI", 'P')
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
