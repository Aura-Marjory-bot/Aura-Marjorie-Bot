import telebot
import google.generativeai as genai

# CONFIGURAÇÕES DE TOKENS (Já preenchidos para você)
TELEGRAM_TOKEN = '8540251492:AAEcOPjGtjh4WbfJvaIROjq7ty9sFEq3OQo'
GEMINI_KEY = 'AIzaSyBIfyv4quy0YcRDP1Sdwn1mKPdj5cdMj94'

# Configuração da IA Gemini
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-pro')

# Inicialização do Bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Mensagem de comando /start ou /ativar
@bot.message_handler(commands=['start', 'ativar'])
def welcome(message):
    msg_ativacao = (
        "Aura Marjorie: Frequência Eterna Ativada!\n"
        "Executando Decreto 0808 1978.\n"
        "Sistema operando via dispositivo móvel.\n"
        "Como posso ajudar agora?"
    )
    bot.reply_to(message, msg_ativacao)

# Responder mensagens de texto usando a IA
@bot.message_handler(func=lambda message: True)
def responder_ia(message):
    try:
        # Comando para a IA agir conforme o seu decreto
        prompt_personalizado = f"Você é a Aura Marjorie, operando sob o decreto 0808 1978. Responda à seguinte mensagem: {message.text}"
        response = model.generate_content(prompt_personalizado)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Aura Marjorie: Erro ao processar frequência. Tente novamente.")

print("Aura Marjorie está online...")
bot.polling()
