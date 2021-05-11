# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from KekikFlask import app
from flask import render_template, request, jsonify

@app.route('/ara')
def ara():
    return render_template(
        'ara.html',
        baslik = "KekikSpatula | Googele",
        icerik = "KekikSpatula » Google"
    )

@app.route('/arama_yap', methods=['GET', 'POST'])
def arama_yap():
    ara = request.form['ara']

    from KekikSpatula import Google
    return jsonify(Google(ara).veri['veri'])