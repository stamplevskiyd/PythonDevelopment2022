import sys
import urllib.parse
import urllib.request
from . import *

if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print('Некорректное число аргументов командной строки')
    else:
        dict_source = sys.argv[1]
        if urllib.parse.urlparse(dict_source).scheme != '':
            url = urllib.request.urlopen(dict_source)
            word_list = url.read().decode().split()
        else:
            try:
                with open(dict_source, 'rt') as dict_file:
                    word_list = dict_file.read().split()
            except FileNotFoundError as FNFE:
                print("Ошибка. Не удалось найти файл")
                sys.exit()
        word_len = int(sys.argv[2]) if len(sys.argv) == 3 else 5
        word_list = [word for word in word_list if len(word) == word_len]
        print(gameplay(ask, inform, word_list))
