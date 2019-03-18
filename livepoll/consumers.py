
from channels import Group
import threading
import random


def periodic():
    global t

    x = random.randint(10, 200)
    sendmsg(str(x))
    t = threading.Timer(0.5, periodic)
    t.start()


def sendmsg(num):
    Group('random').send({'text': num})


t = 0


def ws_message(message):
    global t
    print(message.content['text'])
    if (message.content['text'] == 'start'):
        periodic()
    else:
        t.cancel()


def ws_connect(message):
    Group('random').add(message.reply_channel)
    Group('random').send({'text': 'connected'})


def ws_disconnect(message):
    Group('random').send({'text': 'disconnected'})
    Group('random').discard(message.reply_channel)
