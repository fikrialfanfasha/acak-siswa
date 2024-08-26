from flask import Flask, jsonify, render_template
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
    random.shuffle(siswa)

    kelompok = [[] for _ in range(6)]

    for i, siswa_data in enumerate(siswa):
        kelompok[i % 6].append({'nama': siswa_data['nama'], 'gender': siswa_data['gender']})

    response_data = [{'kelompok': i+1, 'anggota': kelompok[i]} for i in range(6)]
    
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
