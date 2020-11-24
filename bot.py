from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from io import BytesIO
import os
import re
import json

updater = Updater(token='YOUR_TELEGRAM_TOKEN', use_context=True)
dispatcher = updater.dispatcher
bash_command_pay = "java -cp ./takamakachain-1.0-SNAPSHOT-jar-with-dependencies.jar " \
                   " -Djava.awt.headless=true " \
                   "com.h2tcoin.takamakachain.main.DirectCall -e=test -w=walletIsacco -s=asdasdasd -i=0 -p=\"{} 10 " \
                   "10\" -m=\"telegram_user_id={}telegram_user_name={}\" "

bash_command_sign = "java -cp ./takamakachain-1.0-SNAPSHOT-jar-with-dependencies.jar " \
                    " -Djava.awt.headless=true " \
                    "com.h2tcoin.takamakachain.main.DirectCall -e=test -w=walletIsacco -s=asdasdasd -i=0 -v="


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm the Takamaka bot, please talk to "
                                                                    "me!\n\n/charge <ADDRESS>\n\nYou can also upload "
                                                                    "a file in order to get the trusted timestamp")


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


def charge(update, context):
    m = re.search('[0-9a-zA-Z\.\_\-]{44}', context.args[0])
    context.bot.send_message(chat_id=update.message.from_user.id, text='Hi @' + str(
        update.message.from_user.first_name) + ' your request is being processed!')

    if m is not None:
        os.system(bash_command_pay.format(m.group(0), update.message.from_user.id, update.message.from_user.first_name))
    else:
        context.bot.send_message(chat_id=update.message.from_user.id, text='You address is invalid, try again')


def process_file(file, update, context):
    if len(file.file_path) > 0:
        json_passed_param = '{"sourceFileURL":"' + file.file_path + '","retrivalMetadata":"' + 'telegram_user_id=' + str(
            update.message.from_user.id) + 'telegram_user_name=' + str(
            update.message.from_user.first_name) + '","destinationDirectoryPath":"{$YOUR_PATH}blockchain-oracle-telegram/uploaded_files/","tags":["upload_file_trx","telegram_user_id=' + str(
            update.message.from_user.id) + '","telegram_user_name=' + update.message.from_user.first_name + '"]}'
        os.system(
            bash_command_sign.format(update.message.from_user.id, update.message.from_user.first_name) + json.dumps(
                json_passed_param))
    context.bot.send_message(chat_id=update.message.from_user.id,
                             text='Thank you @' + update.message.from_user.first_name + ', your request will be processed as soon as possible!')


def photo(update, context):
    file = context.bot.get_file(update.message.photo[-1].file_id)
    process_file(file, update, context)


def audio(update, context):
    file = context.bot.get_file(update.message.audio.file_id)
    process_file(file, update, context)


def document(update, context):
    file = context.bot.get_file(update.message.document.file_id)
    process_file(file, update, context)


def voice(update, context):
    file = context.bot.get_file(update.message.voice.file_id)
    process_file(file, update, context)


def video(update, context):
    file = context.bot.get_file(update.message.video.file_id)
    process_file(file, update, context)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

pay_handler = CommandHandler('charge', charge)
dispatcher.add_handler(pay_handler)

photo_handler = MessageHandler(Filters.photo, photo)
dispatcher.add_handler(photo_handler)

document_handler = MessageHandler(Filters.document, document)
dispatcher.add_handler(document_handler)

audio_handler = MessageHandler(Filters.audio, audio)
dispatcher.add_handler(audio_handler)

voice_handler = MessageHandler(Filters.voice, voice)
dispatcher.add_handler(voice_handler)

video_handler = MessageHandler(Filters.video, video)
dispatcher.add_handler(video_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
