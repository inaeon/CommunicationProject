import os

PIPE_PATH = '/tmp/my_pipe'


""" communication part """

def create_pipe():
    if not os.path.exists(PIPE_PATH):
        os.mkfifo(PIPE_PATH)


def send_message(message):
    with open(PIPE_PATH, 'w') as pipe:
        pipe.write(message)


def rcv_message():
    with open(PIPE_PATH, 'r') as pipe:
        return pipe.read()



