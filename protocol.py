import socket
LEN_LEN = 4


def padding(num):
    return str(num).zfill(4)


def build(command, args):
    """
    :param command:
    :param args:
    :return:
    [len-cmd(4) + cmd + len-payload(4) + arg$arg$arg$]
    """

    payload = '$'.join(args)

    return f"{padding(len(command))}{command}{padding(len(payload))}{payload}".encode()


def unpack(my_socket):
    """
    :param my_socket:
    :return: unpack the protocol to a command(str) and args(list)
    """
    len_cmd = my_socket.recv(4).decode().lstrip('0')
    cmd = my_socket.recv(int(len_cmd))
    len_args = int(my_socket.recv(4).decode().lstrip('0'))
    args = my_socket.recv(len_args)

    return cmd.decode(), args.split(b'$')



