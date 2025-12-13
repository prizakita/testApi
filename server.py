from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

def InvioWebHook(WebHook):
    url = WebHook

    data = {}

    data["embeds"] = [
        {
            "title": "PROMOZIONE",
            "description": "Aggiornamento rank effettuato con successo!",
            "color": 3066993,
            "fields": [
            ],
            "footer": {
                "text": "Lordine's Projects, Ranker 1"
            },
        }
    ]

    result = requests.post(url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print(f"Payload delivered successfully, code {result.status_code}.")

InvioWebHook("https://discord.com/api/webhooks/1448663497096298638/13DH2mZ_G9Hfq37qh3eBLaTA6mpZEX3KXa_9WTkujUkq6F77Tc0_c4PA_q3ouIPZt8M1")
