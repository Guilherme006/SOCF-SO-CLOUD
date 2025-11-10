import os
import platform
import psutil
from flask import Flask, jsonify

APP = Flask(__name__)

xintegrantes = os.environ.get(
    "INTEGRANTES",
    "Guilherme Felippe Lazari; Danillo Gonçalves Camargo da Silva"
)

def xformatar_sistema_operacional() -> str:
    xsistema = platform.system()
    xplat = platform.platform()
    if "Ubuntu" in xplat:
        return f"{xsistema} (Ubuntu)"
    return xsistema

def xcoletar_metricas():
    xproc = psutil.Process(os.getpid())
    xmem_mb = xproc.memory_info().rss / (1024 ** 2)
    xcpu_pct = xproc.cpu_percent(interval=0.1)
    return {
        "Nome": xintegrantes,
        "PID": xproc.pid,
        "Memoria_MB": round(xmem_mb, 2),
        "CPU": round(xcpu_pct, 2),
        "Sistema_Operacional": xformatar_sistema_operacional(),
    }

@APP.get("/info")
def xinfo():
    return jsonify({"integrantes": xintegrantes})

@APP.get("/metricas")
def xmetricas():
    return jsonify(xcoletar_metricas())

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
