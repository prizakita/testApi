from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

WEBHOOK_URL = os.getenv("https://discord.com/api/webhooks/1448663497096298638/13DH2mZ_G9Hfq37qh3eBLaTA6mpZEX3KXa_9WTkujUkq6F77Tc0_c4PA_q3ouIPZt8M1")

@app.route("/testbello", methods=["POST", "GET"])
def roblox_event():
    # evitare errore 415
    data = request.get_json(silent=True) or {}

    # sicurezza: controlla se il webhook esiste

    requests.post(WEBHOOK_URL, json={
        "content": f"Nuovo evento"
    })

    
    if WEBHOOK_URL:
        requests.post(WEBHOOK_URL, json={
            "content": f"Nuovo evento: {data}"
        })
    else:
        print("NESSUN WEBHOOK SETTATO")

    return {"ok": True, "data": data}

