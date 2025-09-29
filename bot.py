from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import random
import os

# Token vem de variável de ambiente (segurança)
TOKEN = os.getenv("BOT_TOKEN")

RESPOSTAS = [
    "Entendi! 👍",
    "Boa pergunta 🤔",
    "Estou aqui para ajudar 🚀",
    "Interessante! Me fale mais.",
    "Ok, registrado ✅",
    "Haha 😄, gostei da sua mensagem!"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Olá! Eu sou seu bot. Pergunte qualquer coisa que eu respondo!")

async def auto_responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    resposta = random.choice(RESPOSTAS)
    await update.message.reply_text(resposta)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_responder))
    print("✅ Bot rodando no Railway em modo polling...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
