import os
import shutil
from PIL import Image
from zipfile import ZipFile


def zip_name(number):
    return 'flag_' + str(number) + '.zip'


def unzip(number, str_pwd):
    zipname = zip_name(number)
    with ZipFile(zipname) as zf:
        zf.extractall(pwd=bytes(str_pwd,'utf-8'))
    del_file(zipname)
    del_file('pwd.png')
    mov_file(number - 1)
    del_dir('flag')


def mov_file(number):
    os.rename('C:\\Users\\Daniel\\Downloads\\M0rsarchive\\flag\\pwd.png', 'C:\\Users\\Daniel\\Downloads\\M0rsarchive\\pwd.png')
    zipname = zip_name(number)
    os.rename('C:\\Users\\Daniel\\Downloads\\M0rsarchive\\flag\\' + zipname,
              'C:\\Users\\Daniel\\Downloads\\M0rsarchive\\' + zipname)


def del_file(name):
    if os.path.exists(name):
        os.remove(name)


def del_dir(name):
    if os.path.exists(name):
        shutil.rmtree(name)


# this function is written by ZJJ, piece of shit
def get_pwd(passwd_path):
    image = Image.open(passwd_path)
    pixel_data = image.load()
    width, height = image.size
    ori = pixel_data[0, 0]
    arr = []
    for y in range(height):
        li = []
        temp = 0
        for x in range(width):
            if pixel_data[x, y] == ori:
                li.append(temp)
                temp = 0
            else:
                temp += 1
        li = [i for i in li if i != 0]
        if li != []:
            arr.append(li)

    cipher = ''
    for i in arr:
        for j in i:
            if j == 3:
                cipher += '-'
            elif j == 1:
                cipher += '.'
        cipher += ' '

    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
        '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
        ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
        '$': '...-..-', '@': '.--.-.', ' ': '/'
    }

    message = ''
    cipher = cipher.split(' ')
    for code in cipher:
        for char, morse in morse_dict.items():
            if morse == code:
                message += char
    return message.lower()



if __name__ == '__main__':
    for i in range(999, -1, -1):
        str_pwd = get_pwd('pwd.png')
        unzip(i, str_pwd)
