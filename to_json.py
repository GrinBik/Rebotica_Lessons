# Для Discord бота создается файл .json с содержанием всей ненормативной лексики
import json


# Итоговый список всех нецензурных слов для записи в файл
arr = []

# Читаем файл формата .txt с перечнем бранных слов
with open('discord_swear_words.txt', encoding='UTF-8') as file:
    # В каждой строке лишь одно слово, которое и является матом
    for line in file:
        # Считываем мат
        word = line.lower().split('\n')[0]
        # Добавляем новое слово в итоговый перечень
        if word != '' and word not in arr:
            arr.append(word)

# Записываем файл для бота
with open('discord_swear_words.json', 'w', encoding='UTF-8') as write_file:
    json.dump(arr, write_file)