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
def log_ver(istek):
    konsol.log(f"[green]IP Bilgisi :[/] [bold red]{istek.environ.get('HTTP_X_REAL_IP', istek.remote_addr)}[/]  [blue]--[/]  [green]{istek.method} :[/] [bold yellow]{istek.host_url[:-1]}{istek.full_path}[/]", highlight=False)
    # konsol.log(f"[bold red]{istek.environ.get('HTTP_X_REAL_IP', istek.remote_addr)}[/]  [blue]--[/] [bold yellow]{istek.full_path}[/]", highlight=False)

from flask import Flask
from flask_sitemap import Sitemap

app = Flask(__name__)
ext = Sitemap(app=app)

app.config['JSON_SORT_KEYS']                       = False
app.config['JSONIFY_PRETTYPRINT_REGULAR']          = True
app.config['JSON_AS_ASCII']                        = False
app.config['SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS'] = True

from KekikFlask._endpointler import _hata, ana_sayfa, ara