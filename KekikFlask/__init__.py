# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from KekikTaban import KekikTaban

taban = KekikTaban(
    baslik   = "@KekikAkademi KekikFlask",
    aciklama = "KekikFlask Başlatıldı..",
    banner   = "KekikFlask",
    girinti  = 4
)

konsol = taban.konsol

def onemli(yazi):
    konsol.print(yazi, style="bold cyan", width=70, justify="center")

from flask import Flask
from flask_sitemap import Sitemap

app = Flask(__name__)
ext = Sitemap(app=app)

app.config["JSON_SORT_KEYS"]                       = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"]          = True
app.config["JSON_AS_ASCII"]                        = False
app.config["SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS"] = True

from os import urandom
app.secret_key = urandom(16)

from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, set_access_cookies
import random, string

app.config['JWT_SECRET_KEY']          = ''.join(random.choice(string.ascii_lowercase) for i in range(22))
app.config['JWT_TOKEN_LOCATION']      = ['cookies']
app.config['JWT_COOKIE_SECURE']       = True
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
#app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/'
flask_jwt = JWTManager(app)

from jwt import encode, decode
jwt_encode = lambda mail  : encode({"mail": mail}, app.config['SECRET_KEY'], algorithm="HS512")
jwt_decode = lambda token : decode(token, app.config['SECRET_KEY'], algorithms=["HS512"])

from typing import Dict

def ip_log(hedef_ip:str) -> Dict[str, str]:
    from requests import get

    url    = f"http://ip-api.com/json/{hedef_ip}"
    istek  = get(url).json()

    if istek['status'] != 'fail':
        return {
            'ulke'     : istek['country'] or '',
            'il'       : istek['regionName'] or '',
            'isp'      : istek['isp'] or '',
            'sirket'   : istek['org'] or '',
            'host'     : istek['as'] or ''
        }
    else:
        return {'hata': 'Veri Bulunamadı..'}

from time import time
from flask import g, request, session, Response
from user_agents import parse
from json import loads

@app.before_request
def zamanlayici_baslat():
    g.start = time()

@app.after_request
def istek_log(yanit:Response) -> Response:
    if (request.path == "/favicon.ico") or (request.path.startswith("/static")) or (request.path.startswith("/monitor")):
        return yanit

    simdi = time()

    try:
        if str(parse(request.headers.get('User-Agent'))).split('/')[2].strip() == 'Other':
            cihaz = request.headers.get('User-Agent')
        else:
            cihaz = parse(request.headers.get('User-Agent'))
    except TypeError:
        cihaz = request.headers.get('User-Agent')

    try:
        log_ip = request.environ['HTTP_X_FORWARDED_FOR'] or request.environ['REMOTE_ADDR']
    except KeyError:
        log_ip = request.remote_addr

    log_veri = {
        'id'     : session.get('kullanici_id') or '', 
        'method' : request.method,
        'url'    : request.host_url[:-1] + request.full_path,
        # 'data'   : (request.form.to_dict()) or (loads(request.data) if request.data else None),
        'data'   : request.data or request.form.to_dict(),
        'kod'    : yanit.status_code,
        'sure'   : round(simdi - g.start, 2),
        'ip'     : log_ip,
        'cihaz'  : cihaz,
        'host'   : request.host.split(":", 1)[0],
    }

    if request.headers.get("X-Request-ID"):
        log_veri.update({"id" : request.headers.get("X-Request-ID")})

    endpoint_bilgisi = f"[bold blue]»[/] [bold turquoise2]{log_veri['url']}[/]"
    data_bilgisi     = f"[blue]|[/] [green]data:[/] [bold turquoise2]{log_veri['data']}[/]" if log_veri['data'] else ""

    konsol.log(f"{endpoint_bilgisi} {data_bilgisi}")
    konsol.log(f"[bold bright_blue]{log_veri['id']}[/][bold green]@[/][bold red]{log_veri['ip']}[/]\t[blue]|[/] [green]cihaz:[/] [magenta]{log_veri['cihaz']}[/] [blue]|[/] [bold green]{log_veri['method']}[/] [blue]-[/] [bold bright_yellow]{log_veri['kod']}[/] [blue]-[/] [bold yellow2]{log_veri['sure']}sn[/]")

    ip_detay = ip_log(log_veri['ip'])
    if ('hata' not in list(ip_detay.keys())) and (ip_detay['ulke']):
        konsol.log(f"[bold chartreuse3]{ip_detay['ulke']}[/] [blue]|[/] [bold chartreuse3]{ip_detay['il']}[/] [blue]|[/] [bold chartreuse3]{ip_detay['sirket']}[/] [blue]|[/] [bold chartreuse3]{ip_detay['isp']}[/] [blue]|[/] [bold chartreuse3]{ip_detay['host']}[/]")

    return yanit

####
from KekikFlask._endpointler import _hata, ana_sayfa, ara
