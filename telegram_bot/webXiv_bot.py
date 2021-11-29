#!/usr/bin/env python3

from telegram.ext import Updater
import logging
from telegram import Update, message
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
import requests
import time
from dotenv import load_dotenv
import os

inbox_path = 'http://alussana.xyz/Xiv/inbox/inbox.txt'

load_dotenv()
token = os.getenv('TOKEN')
user = int(os.getenv('AUTHORIZED_USER'))
inbox_path = '/usr/share/nginx/html/inbox/inbox.txt'

updater = Updater(
        token=token,
        use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

def start(update: Update, context: CallbackContext):
    chat_id = get_chat_id(update=update, context=context)
    user_id = update.effective_user.id
    if user_id == user:
        update.message.reply_text('Hi! I will notify you of new messages. I am fetching the latest one now, see below...')
        monitor_inbox(chat_id)
    else:
        update.message.reply_text('You are not authorized to talk with me.')
        exit

def monitor_inbox(chat_id):
    latest_message_time = -1
    while True:
        time.sleep(30)
        message_time = get_latest_message_time()
        if message_time != latest_message_time:
            latest_message_time = message_time
            print_latest_message(chat_id)

def get_chat_id(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    return(chat_id)

def get_latest_message_time():
    with open(inbox_path) as inbox_fh:
        inbox = inbox_fh.readlines()
    inbox = ''.join(inbox)
    mails = inbox.split("--")
    mail = mails[len(mails) -1]
    time_field = mail.split('|_|')[0]
    time = time_field.split(': ')[1]
    return(time)

def print_latest_message(chat_id: str):
    with open(inbox_path) as inbox_fh:
        inbox = inbox_fh.readlines()
    inbox = ''.join(inbox)
    mails = inbox.split("--")
    mail = mails[len(mails) -1]
    fields = mail.split('|_|')
    mex = ''.join(fields)
    updater.bot.send_message(
            chat_id = chat_id,
            text = mex)

def latest_message(update: Update, context: CallbackContext ):
    with open(inbox_path) as inbox_fh:
        inbox = inbox_fh.readlines()
    inbox = ''.join(inbox)
    mails = inbox.split("--")
    context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=mails[len(mails) -1])

def remote_get_latest_message_time():
    r = requests.get(
            inbox_path,
            auth=(username, password))
    mails = r.text.split("--")
    mail = mails[len(mails) -1]
    time_field = mail.split('|_|')[0]
    time = time_field.split(': ')[1]
    return(time)

def remote_print_latest_message(chat_id: str):
    r = requests.get(
            inbox_path,
            auth=(username, password))
    mails = r.text.split("--")
    mail = mails[len(mails) -1]
    fields = mail.split('|_|')
    mex = ''.join(fields)
    updater.bot.send_message(
            chat_id = chat_id,
            text = mex)

def remote_latest_message(update: Update, context: CallbackContext ):
    r = requests.get(
            inbox_path,
            auth=(username, password))
    mails = r.text.split("--")
    context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=mails[len(mails) -1])

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
latest_message_handler = CommandHandler('latest_message', latest_message)
dispatcher.add_handler(latest_message_handler)

updater.start_polling()
