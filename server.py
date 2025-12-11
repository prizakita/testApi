from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

DISCORD_WEBHOOK = os.environ.get("https://discord.com/api/webhooks/1448663497096298638/13DH2mZ_G9Hfq37qh3eBLaTA6mpZEX3KXa_9WTkujUkq6F77Tc0_c4PA_q3ouIPZt8M1")

@app.route("/roblox", methods=["POST"])
def roblox_event():
    try:
        data = request.json

        # Messaggio base
        message = {
            "content": f"Evento da Roblox:\n```json\n{data}\n```"
        }

        # Invia il messaggio a Discord
        r = requests.post(DISCORD_WEBHOOK, json=message)
        return jsonify({"status": r.status_code}), r.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/")
def home():
    return "Server Render attivo"

