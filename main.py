import datetime
import hashlib
import logging
import os


def with_logging(func):
    path_log = f"log\\"

    def wrap_log(*args, **kwargs):
        nonlocal path_log

        try:
            os.mkdir(path_log)
        except OSError:
            pass

        name = func.__name__
        logging.basicConfig(filename=os.path.join(path_log, f'log.txt'), level=logging.INFO)
        result = func(*args, **kwargs)
        logging.info(f'{datetime.datetime.now().replace(microsecond=0)} Вызов функции: {name}, Результат: {result}\n')
        return func(*args, **kwargs)

    return wrap_log


@with_logging
def hash_lines(filename):
    try:
        with open(filename, 'rb') as datafile:
            m = hashlib.md5()
            line = datafile.readline()
            while line:
                m.update(line)
                line = datafile.readline()
                yield m.hexdigest()
    except FileNotFoundError as text_error:
        print(text_error)


if __name__ == '__main__':
    for number, hash_line in enumerate(hash_lines(input('Введите путь к файлу для хеширования: ')), 1):
        print(f'{number}: {hash_line}')