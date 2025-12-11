from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

@app.route("/testbello", methods=["POST", "GET"])
def roblox_event():
    # evitare errore 415
    data = request.get_json(silent=True) or {}

    # sicurezza: controlla se il webhook esiste
    if WEBHOOK_URL:
        requests.post(WEBHOOK_URL, json={
            "content": f"Nuovo evento: {data}"
        })
    else:
        print("NESSUN WEBHOOK SETTATO")

    return {"ok": True, "data": data}

