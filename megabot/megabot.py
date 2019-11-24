from telegram.ext import Updater, CommandHandler

PROXY={'proxy_url':'socks5://t1.learn.python.ru:1080','urllib3_proxy_kwargs':{'username':'learn','password':'python'}}

def main():
    mybot = Updater("847346869:AAFIH71Nsondocu8C3gh6gQUx2EXWFmUmds",request_kwargs=PROXY)
    dp=mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    mybot.start_polling()
    mybot.idle()

def greet_user(bot,update):
    print('Вызван старт')
main()