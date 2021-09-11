# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from KekikFlask import app
from flask import render_template, request, jsonify
from flask_jwt_extended import jwt_required

@app.route('/ara')
@jwt_required()
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