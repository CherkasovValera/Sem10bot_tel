from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async    def log(update: Update, context: ContextTypes.DEFAULT_TYPE) -> object:
             file = open('db.csv','a')
             file.write(f'{update.effective_user.first_name},{update.effective_user.id},{update.masssage.text}\n')
             file.close()
    # await update.message.reply_text(f'{datetime.datetime.now().time()}')
