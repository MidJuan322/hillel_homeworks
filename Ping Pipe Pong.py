from multiprocessing import Process, Pipe
from time import sleep
from os import getpid


def ponger(sender, response):
    dict_msg = {'ping': 'pong', 'pong': 'ping'}
    while True:
        msg = response.recv()
        print(f"Process{getpid()} got message: {dict_msg[msg]}")
        sleep(1)
        sender.send(dict_msg[msg])


if __name__ == "__main__":
    parent_conn_1, child_conn_1 = Pipe()

    process_1 = Process(target=ponger, args=(parent_conn_1, child_conn_1))
    process_2 = Process(target=ponger, args=(parent_conn_1, child_conn_1))

    parent_conn_1.send('pong')

    process_1.start()
    process_2.start()