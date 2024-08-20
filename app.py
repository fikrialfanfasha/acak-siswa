from flask import Flask, jsonify, request, render_template
import random

app = Flask(__name__)

siswa = [
    ("AGUNG PRASETIO", 'L'), ("ARIMA RAHAYU", 'P'), ("MUHAMAD IQBAL", 'L'),
    ("PRADITYA TRI ANNISAA", 'P'), ("RAHMANIAH AL PRIATNA", 'P'), 
    ("REZA SUBAGJA", 'L'), ("ANITA LUVITA", 'P'), ("ASIS MAULANA", 'L'),
    ("DHERA FRASETYO. S", 'L'), ("DIANDRA FAUZI RAMADHANI", 'L'), 
    ("DZIKRA AHSAN IMAWAN", 'L'), ("GHEFIRA NUR FATIMAH", 'P'),
    ("JANTRA REISA ALFAYIZ SUPRIATNA", 'L'), ("KEISYA RAMADHINA PUTRI", 'P'),
    ("MUHAMAD FAUZI RIDWAN", 'L'), ("MUHAMMAD HAIKAL AL MACCA", 'L'),
    ("RAKHA MUHAMAD FATAN", 'L'), ("SUTINI NURAENI ELI HANDAYANI", 'P'),
    ("ADE NURMILASARI", 'P'), ("AINI RIZKA NUR AFIFAH", 'P'),
    ("GEASTRID DWY DESTRIAN", 'P'), ("MUHAMAD FARHAN HIBATULLAH", 'L'),
    ("NESYRIN SYAHARANI FAZRI", 'P'), ("NURIDA SUSAN NIARDJIE", 'P'),
    ("SITI FAZRI AROHMAH", 'P'), ("VIKA EVANTHI", 'P'),
    ("AEP SAEPUDIN ANWAR", 'L'), ("BALQIS HANIFA", 'P'),
    ("DAFFA ISLAMY PASHAA", 'L'), ("DEDE YUSUF NUR KHOLIK", 'L'),
    ("LUTFI FADHILLATUN RAMADAN", 'L'), ("MUHAMMAD FAKHRI ALGHIFARI", 'L'),
    ("NABIL ALI WIBOWO", 'L'), ("SUSILAWATI", 'P'),
    ("TITA SUMARNI", 'P'), ("WULANSARI", 'P')
]

ketua_kelompok = [
    "MUHAMAD IQBAL", "MUHAMMAD HAIKAL AL MACCA", "MUHAMAD FAUZI RIDWAN",
    "DIANDRA FAUZI RAMADHANI", "MUHAMAD FARHAN HIBATULLAH", "RAKHA MUHAMAD FATAN"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/daftar-siswa')
def daftar_siswa():
    return jsonify([{'nama': nama, 'gender': gender} for nama, gender in siswa])

@app.route('/buat-kelompok', methods=['POST'])
def buat_kelompok():
    siswa_laki = [nama for nama, gender in siswa if gender == 'L' and nama not in ketua_kelompok]
    siswa_perempuan = [nama for nama, gender in siswa if gender == 'P']
    
    random.shuffle(siswa_laki)
    random.shuffle(siswa_perempuan)
    random.shuffle(ketua_kelompok)

    kelompok = [[] for _ in range(6)]
    for i, ketua in enumerate(ketua_kelompok):
        kelompok[i].append({'nama': ketua, 'jabatan': 'Ketua', 'gender': dict(siswa).get(ketua, 'Tidak diketahui')})

    for i in range(6):
        while len(kelompok[i]) < 6:
            if len([s for s in kelompok[i] if s['gender'] == 'L']) < 3 and siswa_laki:
                kelompok[i].append({'nama': siswa_laki.pop(0), 'jabatan': 'Anggota', 'gender': 'L'})
            elif len([s for s in kelompok[i] if s['gender'] == 'P']) < 3 and siswa_perempuan:
                kelompok[i].append({'nama': siswa_perempuan.pop(0), 'jabatan': 'Anggota', 'gender': 'P'})
            else:
                break

    for i in range(6):
        while len(kelompok[i]) < 6:
            if siswa_laki:
                kelompok[i].append({'nama': siswa_laki.pop(0), 'jabatan': 'Anggota', 'gender': 'L'})
            elif siswa_perempuan:
                kelompok[i].append({'nama': siswa_perempuan.pop(0), 'jabatan': 'Anggota', 'gender': 'P'})
    
    response_data = [{'kelompok': i+1, 'anggota': sorted(grup, key=lambda x: x['jabatan'])} for i, grup in enumerate(kelompok)]
    
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
