import time
import requests

# Token e ID do seu bot
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Erro ao enviar mensagem:", e)

def buscar_arbitragem():
    # Simulação de alerta — aqui entra a lógica real depois
    oportunidades = [
        {"evento": "Flamengo x Palmeiras", "lucro": "6.3%", "mercado": "1X2"},
        {"evento": "Manchester x Arsenal", "lucro": "5.1%", "mercado": "Over/Under"}
    ]
    return oportunidades

def rodar_bot():
    while True:
        oportunidades = buscar_arbitragem()
        for oportunidade in oportunidades:
            msg = (
                f"📢 OPORTUNIDADE DE ARBITRAGEM!\n\n"
                f"🏟 Evento: {oportunidade['evento']}\n"
                f"💸 Lucro: {oportunidade['lucro']}\n"
                f"🎯 Mercado: {oportunidade['mercado']}"
            )
            send_alert(msg)
        time.sleep(3600)  # Espera 1 hora (ajuste conforme necessário)

if __name__ == "__main__":
    send_alert("🤖 Bot de Arbitragem iniciado com sucesso!")
    rodar_bot()
