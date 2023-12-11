import glob
import os
import shutil
import subprocess
import base64
import pyautogui


def assert_dir(file):
     try:
        file = file[0]
        my_file = file + '/*.*'
        file_dir = glob.glob(my_file)
        return str(file_dir)
     except glob.error as err:
        return 'received glob error ' + str(err)

def dir_file(file):
    """

    :param file:
    :return: a list of whats inside the file
    """
    try:
        file = file[0].decode()
        my_file = file + '/*.*'
        file_dir = glob.glob(my_file)
        return str(file_dir)
    except glob.error as err:
        return 'received glob error ' + str(err)


def del_file(file):
    """

    :param file:
    :return: deletes the file or not
    """
    try:
        os.remove(file[0])
        return "file has been removed"
    except os.error as err:
        return 'received os error ' + str(err)


def copy_file(file_list):
    """

    :param file_list:
    :return: tries to copy a file and return: file has been copied
    """
    try:
        shutil.copy(file_list[0], file_list[1])
        return "file has been copied"
    except shutil.error as err:
        return 'received shutil error ' + str(err)


def open_visual(my_path):
    """

    :param my_path:
    :return: if the app has been opened
    """
    try:
        subprocess.call(my_path[0])
        return "app has been opened"
    except subprocess.error as err:
        return 'received subprocess error ' + str(err)


def take_screen():
    """

    :return: the bytes of the image in str
    """
    try:
        image = pyautogui.screenshot()
        image.save(r'/Users/iftach_1kasorla/Documents/proj2.7/screen1.png')
        try:
            with open(r'/Users/iftach_1kasorla/Documents/proj2.7/screen1.png', 'rb') as file:
                image_bytes = file.read()
            encoded_image = base64.b64encode(image_bytes)
            return encoded_image.decode('utf-8')  # Convert bytes to string for transmission
        except base64.error as err:
            return "Error in send_photo: " + str(err)
    except pyautogui.error as err:
        return 'received pyautogui error ' + str(err)


def EXIT():
    """

    :return: EXIT
    """
    return 'EXIT'



