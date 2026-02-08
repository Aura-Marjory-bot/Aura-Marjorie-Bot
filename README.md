# Aura-Marjorie-bot
import os
from flask import Flask
server = Flask(__name__)

@server.route("/")
def webhook():
    return "Aura Marjorie Ativa", 200

if __name__ == "__main__":
    import threading
    threading.Thread(target=bot.polling).start()
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
