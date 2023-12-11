import funk
import protocol
import socket
import logging
import os

IP = '0.0.0.0'
PORT = 8821
QUEUE_LEN = 1

LOG_FORMAT = '%(levelname)s | %(asctime)s | %(message)s'
LOG_LEVEL = logging.DEBUG
LOG_DIR = 'log'
LOG_FILE = LOG_DIR + '/lucky.log'





def what_to_ret(client_socket):
    """
    :param client_socket:
    :return: the function divide the commends and return answers accordingly
    """
    while 1:
        try:
            request = protocol.unpack(client_socket)
            if request[0] == 'dir_file':
                client_socket.send(protocol.build('dir_file', [funk.dir_file(request[1]), '']))

            elif request[0] == 'del_file':
                client_socket.send(protocol.build('del_file', [funk.del_file(request[1]), '']))

            elif request[0] == 'copy_file':
                client_socket.send(protocol.build('copy_file', [funk.copy_file(request[1]), '']))

            elif request[0] == 'open_visual':
                client_socket.send(protocol.build('open_visual', [funk.open_visual(request[1]), '']))

            elif request[0] == 'take_screen':
                client_socket.send(protocol.build('take_screen', [funk.take_screen(), '']))

            elif request[0] == 'EXIT':
                client_socket.close()
                return
        except socket.error as err:
            print('received socket error on client socket' + str(err))
            logging.info('received socket error on client socket' + str(err))
            return


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.debug(IP)
    logging.debug(PORT)
    logging.debug(QUEUE_LEN)
    my_socket.bind((IP, PORT))
    my_socket.listen(QUEUE_LEN)

    try:
        while 1:
            client_socket, client_address = my_socket.accept()

            what_to_ret(client_socket)


    except socket.error as err:

        print('received socket error on server socket' + str(err))
        logging.info('received socket error on client socket' + str(err))

    finally:
        client_socket.close()
        my_socket.close()


if __name__ == '__main__':
    assert protocol.build('dir_file', [r'/Users/iftach_1kasorla/Documents/cyberDemo', '']) == b'0008dir_file0043/Users/iftach_1kasorla/Documents/cyberDemo$'
    if not os.path.isdir(LOG_DIR):
        os.makedirs(LOG_DIR)
    logging.basicConfig(format=LOG_FORMAT, filename=LOG_FILE, level=LOG_LEVEL)
    main()
