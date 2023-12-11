import protocol
import funk
import base64
import socket
import logging
import os

IP = '127.0.0.1'

PORT = 8821

LOG_FORMAT = '%(levelname)s | %(asctime)s | %(message)s'
LOG_LEVEL = logging.DEBUG
LOG_DIR = 'log'
LOG_FILE = LOG_DIR + '/lucky.log'


def is_legal_message(my_message):
    """

    :param my_message: gets the command
    :return: if my message is valid
    """
    return my_message == 'dir_file' or my_message == 'del_file' or my_message == 'copy_file' or my_message == 'open_visual' or my_message == 'take_screen'


def send_message(my_socket):
    """

    :param my_socket:
    :return: there is a loop until the client put EXIT. until then the function sends and receive messages from the server
    """

    while 1:
        what_to_send_funk = input('What funk do you want? ')
        what_to_send_parm = input('What parameters do you want? ')
        what_to_send_parm1 = input('What parameters do you want? ')
        logging.info(what_to_send_funk)
        logging.info(what_to_send_parm)
        logging.info(what_to_send_parm1)
        if is_legal_message(what_to_send_funk):
            my_socket.send(protocol.build(what_to_send_funk, [what_to_send_parm, what_to_send_parm1]))
            if what_to_send_funk == 'dir_file' or what_to_send_funk == 'del_file' or what_to_send_funk == 'copy_file' or what_to_send_funk == 'open_visual':
                my_msg = protocol.unpack(my_socket)[1]
                my_msg = my_msg[0].decode()
                print(my_msg)

            elif what_to_send_funk == 'take_screen':

                my_msg = protocol.unpack(my_socket)[1]
                image_data = base64.b64decode(my_msg[0].decode())
                with open(r'/Users/iftach_1kasorla/Documents/proj2.7/screen2.png', 'wb') as file:
                    file.write(image_data)


        elif what_to_send_funk == 'EXIT':
            my_socket.send(protocol.build(what_to_send_funk, [what_to_send_parm, what_to_send_parm1]))
            print('you left the server')
            return
        else:
            print('Illegal message. Please choose between dir_file / del_file / copy_file / open_visual / take_screen /EXIT')


def main():
    logging.debug(IP)
    logging.debug(PORT)
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        my_socket.connect((IP, PORT))
        send_message(my_socket)

    except socket.error as err:
        print('received socket error ' + str(err))
        logging.error('received socket error on client socket' + str(err))
    finally:

        my_socket.close()


if '__main__' == __name__:
    funk.copy_file([r'/Users/iftach_1kasorla/Documents/proj2.7/README.md', r'/Users/iftach_1kasorla/Documents/proj2.7/README1.md'])
    assert r'/Users/iftach_1kasorla/Documents/proj2.7/README1.md' in funk.dir_file([r'/Users/iftach_1kasorla/Documents/proj2.7', ''])
    funk.del_file([r'/Users/iftach_1kasorla/Documents/cyberDemo/new2.md', ''])
    assert not r'/Users/iftach_1kasorla/Documents/cyberDemo/new2.md' in funk.dir_file([r'/Users/iftach_1kasorla/Documents/proj2.7', ''])

    if not os.path.isdir(LOG_DIR):
        os.makedirs(LOG_DIR)
    logging.basicConfig(format=LOG_FORMAT, filename=LOG_FILE, level=LOG_LEVEL)
    main()
