# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from KekikFlask import app, log_ver
from flask import render_template, request, jsonify

@app.route('/ara')
def ara():
    log_ver(request)

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