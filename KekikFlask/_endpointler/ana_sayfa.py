# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from KekikFlask import app
from flask import render_template, jsonify

@app.route('/')
def ana_sayfa():

    return render_template(
        'ana_sayfa.html',
        baslik = "Merhaba Flask!",
        icerik = "Ben Python Dosyasından Değişken Olarak Geldim.."
    )

@app.route('/veri_takip', methods=['GET', 'POST'])
def veri():
    import random
    return jsonify({'veri': random.randint(50, 50000)})