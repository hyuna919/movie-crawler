import telegram

bot = telegram.Bot(token = '1218021692:AAEiz5oi3qjrSPniksysazIe10JTo-V-gOI')

#for i in bot.getUpdates():
#    print(i.message)

id = 1157929440

bot.sendMessage(chat_id=id, text="hello")