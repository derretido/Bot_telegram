                                                            #Bot para o telegram que envia link de afiliados

from email.mime import application
import os
from telegram.ext import Application,ApplicationBuilder, CommandHandler
from dotenv import load_dotenv
import asyncio
import logging
import datetime
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from pymongo import MongoClient
from zoneinfo import ZoneInfo

# Corrige problema de loop no Windows 
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

#Verificação de logs
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


# Carregar o token do arquivo .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))

#bot = Bot(token=TOKEN) 
#asyncio.run(bot.send_message(chat_id=CHAT_ID, text="Bot conectado com sucesso!"))
#print("Token carregado")

# Configurar conexão com o MongoDB
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["Telegram_bott"]
collection = db["links"]
print(collection.find_one())

# Função para carregar promoções direto do Atlas
def load_promotions():
    return list(collection.find({}, {"_id": 0, "hora": 1, "url": 1}))


#Função para pegar os links de promoção de acordo com a hora
def get_links(hora):
    return next((item["url"] for item in load_promotions() if item["hora"] == hora), None)

keyboard =[
    [InlineKeyboardButton(f"Promoção {i}h", url=get_links(i)) 
    for i in range(9, 19)]
]
reply_markup = InlineKeyboardMarkup(keyboard)
print("Links carregados com sucesso!")

dados = load_promotions()
print("Documentos inseridos:", collection.count_documents({}))
print("Primeiro documento:", collection.find_one())

#Função para iniciar o bot
async def start(update, context):
    await update.message.reply_text("Olá, bem-vindo ao Achadinhos Imperdíveis! Envie /help para ver os comandos disponíveis.")

#Função para ajuda ao usuário
async def help_comand(update, context):
    await update.message.reply_text("Comandos disponíveis:\n/start - Iniciar o bot\n/help - Ver os comandos disponíveis\n/promo - Receber o link de promoção\n/contato - Falar com o suporte\n/info - saber mais sobre Achadinhos Imperdíveis" \
    "\n/feedback - Enviar feedback sobre o produto divulgados")


# função para enviar os links de promoção
async def promo(update, context):
    keyboard = [
        [InlineKeyboardButton(f"Promoção {hora}h", url=get_links(hora))]
        for hora in range(9, 20)  # gera de 9 até 19
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Escolha uma promoção:", reply_markup=reply_markup)

#função para falar com o suporte 
async def contato(update, context):
    await update.message.reply_text("para falar com o suporte, envie uma mensagem o para o numero (11)97711-2443 Envie mensagem apenas no horario comercial e dentro do Telegram,não respondemos mensagens fora do telegram ")

#função para informações sobre Achadinhos Imperdíveis
async def info(update,context):
    await update.message.reply_text("Achadinhos Imperdiveis é um canal de divulgação de promoções e produtos exclusivamente da shoppe\n" \
    "Somos um canal com o objetivo de ajudar nossos seguidores a economizar dinheiro e encontrar as melhores ofertas disponíveis na plataforma da shoppe\n"  
    "Nosso canal é atualizado diariamente." )

#função de feedback para os usuarios enviarem suas sugestões e opiniões sobre os produtos divulgados
async def feedback(update,context):
    await update.message.reply_text("Agradecemos seu interesse em enviar feedback! Por favor fique à vontade de compartilhar novas sugestões, opiniões ou dúvidas sobre os produtos divulgados.")

#função para mostrar o ID do chat, útil para identificar os grupos onde o bot está presente
#async def id(update,context):
#    chat_id = update.message.chat_id
#    await update.message.reply_text(f"Seu ID de chat é: {chat_id}")

#função para enviar mensagens agendadas dentro dos grupos
async def send_scheduled_message(context):
    hora_atual = context.job.data["hora"]
    CHAT_ID = context.job.data["CHAT_ID"]
    links = load_promotions()

    # procurar o link correspondente à hora
    link = next((item["url"] for item in links if item["hora"] == hora_atual), None)

    if link:
        keyboard = [[InlineKeyboardButton(f"Promoção {hora_atual}h", url=link)]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(
            chat_id= CHAT_ID,
            text=f"Confira a promoção das {hora_atual}h:",
            reply_markup=reply_markup
        )


#Configuração do bot
def main():
    application = Application.builder().token(TOKEN).build()

    #Aqui faz a ligação dos comandos com as funções
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help",help_comand))
    application.add_handler(CommandHandler("promo", promo))
    application.add_handler(CommandHandler("contato",contato))
    application.add_handler(CommandHandler("info",info))
    application.add_handler(CommandHandler("feedback",feedback))
#   application.add_handler(CommandHandler("id",id))
    application.add_handler(CommandHandler("send_scheduled_message", send_scheduled_message))


    #Agendamento de mensagens
    brasilia_tz = ZoneInfo('America/Sao_Paulo')
    job_queue = application.job_queue
    horarios = [9,10,11,12,13,14,15,16,17,18,19]  # Hora de envio de mensagens (9h às 19h)
    for hora in horarios:
        job_queue.run_daily(
            send_scheduled_message,
            time=datetime.time(hour=hora, minute=0, second=0, tzinfo=brasilia_tz),
            data={"hora": hora, "CHAT_ID": -5009071096}   
        )
    
    #iniciar o bot
    print("Bot iniciado com sucesso!")
    application.run_polling()

    
if __name__ == "__main__":
    main()