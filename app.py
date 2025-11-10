import os
import json
import platform
import psutil
from flask import Flask, Response

APP = Flask(__name__)

xintegrantes = os.environ.get(
    "INTEGRANTES",
    "Guilherme Felippe Lazari e Danillo Gonçalves Camargo da Silva"
)

def xjson(payload: dict, status: int = 200) -> Response:
    return Response(
        json.dumps(payload, ensure_ascii=False),
        status=status,
        mimetype="application/json; charset=utf-8",
    )

def xformatar_sistema_operacional() -> str:
    return platform.system()

def xcoletar_metricas():
    xproc = psutil.Process(os.getpid())
    xmem_mb = xproc.memory_info().rss / (1024 ** 2)
    xcpu_pct = xproc.cpu_percent(interval=0.1)
    return {
        "Nome": xintegrantes,
        "PID": xproc.pid,
        "Memoria": f"{round(xmem_mb, 2)} MB",
        "CPU": f"{round(xcpu_pct, 2)}%",
        "Sistema_Operacional": xformatar_sistema_operacional(),
    }

@APP.get("/info")
def xinfo():
    return xjson({"integrantes": xintegrantes})

@APP.get("/metricas")
def xmetricas():
    return xjson(xcoletar_metricas())

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
