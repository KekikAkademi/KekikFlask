# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from KekikFlask import app, onemli
from os import environ

port = int(environ.get("PORT", 5000))
host = "0.0.0.0"

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = port)

    onemli(f'\nKekikFlask [bold red]{host}[yellow]:[/]{port}[/]\'de başlatılmıştır...\n')

    # from waitress import serve
    # serve(app, host = host, port = port)