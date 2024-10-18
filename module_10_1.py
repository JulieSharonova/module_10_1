from datetime import datetime
from threading import Thread
from time import sleep

time_start = datetime.now()


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            word = f'Какое-то слово № {i}\n'
            file.write(word)
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков: {time_res}')

time_start = datetime.now()

write_words_5 = Thread(target=write_words, args=(10, 'example5.txt'))
write_words_6 = Thread(target=write_words, args=(30, 'example6.txt'))
write_words_7 = Thread(target=write_words, args=(200, 'example7.txt'))
write_words_8 = Thread(target=write_words, args=(100, 'example8.txt'))

write_words_5.start()
write_words_6.start()
write_words_7.start()
write_words_8.start()

write_words_5.join()
write_words_6.join()
write_words_7.join()
write_words_8.join()

time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков: {time_res}')
