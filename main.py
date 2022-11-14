
from bot_commands import *



app = ApplicationBuilder().token("5466100628:AAF6NEj5TVg-6ZDBTNhfH_5CH_5sLR_e8bI").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("mult", mult_command))
app.add_handler(CommandHandler("diff", diff_command))
app.add_handler(CommandHandler("del", del_command))
print("Gut")
app.run_polling()

