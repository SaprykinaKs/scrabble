eng = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}

rus = {
    'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
    'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
    'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
    'Й': 4, 'Ы': 4,
    'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
    'Ш': 8, 'Э': 8, 'Ю': 8,
    'Ф': 10, 'Щ': 10, 'Ъ': 10
}

# игровое поле 5x5 с бонусами
# * = обычная клетка, # = x2 буква, & = x2 слово
board = [
    ['*', '*', '#', '*', '*'],
    ['*', '&', '*', '&', '*'],
    ['#', '*', '*', '*', '#'],
    ['*', '&', '*', '&', '*'],
    ['*', '*', '#', '*', '*'],
]

# вывод поля
def print_board():
    print("Текущее состояние поля:")
    for row in board:
        print(' '.join(row))
    print()

# проверка слова
def valid(word, language):
    word = word.upper()  
    if language == 'english':
        return all(char in eng for char in word)
    elif language == 'russian':
        return all(char in rus for char in word)
    else:
        return False
    
# проверка на перезапись букв
def can_place(word, start_row, start_col, direction):
    word = word.upper()

    for i, char in enumerate(word):
        row = start_row + i if (direction == 'v' or direction == 'в')  else start_row
        col = start_col + i if (direction == 'h' or direction == 'г') else start_col

        if board[row][col].isalpha() and board[row][col] != char:
            return False  # клетка занята другой буквой
    return True

# подсчет
def calc(word, language, start_row, start_col, direction):
    word = word.upper()
    scores = eng if language == 'english' else rus
    score = 0
    multiplier = 1  

    for i, char in enumerate(word):
        # находим текущую клетку
        row = start_row + i if (direction == 'v' or direction == 'в') else start_row
        col = start_col + i if (direction == 'h' or direction == 'г') else start_col
        
        cell = board[row][col] # тип клетки
        letter_score = scores[char]  

        # бонусы
        if cell == '#':  
            letter_score *= 2
        elif cell == '&': 
            multiplier *= 2
        
        score += letter_score

    return score * multiplier  

# размещение слова
def place_on_board(word, start_row, start_col, direction):
    word = word.upper()
    
    for i, char in enumerate(word):
        row = start_row + i if (direction == 'v' or direction == 'в') else start_row
        col = start_col + i if (direction == 'h' or direction == 'г') else start_col
        board[row][col] = char  # размещаем букву 

# выбор языка
def choose_language():
    while True:
        lang = input("выберите язык игры (введите 'ru'/'ру' для русского или 'en'/'англ' для английского): ").lower()
        if lang == 'ru' or lang == 'ру':
            return 'russian'
        elif lang == 'en' or lang == 'англ':
            return 'english'
        else:
            print("ошибка: выберите 'ru'/'ру' для русского или 'en'/'англ' для английского")

# 
def play_game():
    language = choose_language()  # выбор языка
    total_score = 0
    print("Обозначения: '*' = обычная клетка, '#' = бонус x2 на букву, '&' = бонус x2 на слово")
    while True:
        print_board()  # текущее состояние поля
    
        word = input("введите слово (или 'стоп'/'stop' для завершения): ")
        if word.lower() == 'стоп' or word.lower() == 'stop':
            break

        if not valid(word, language):
            print("ошибка: слово должно содержать только буквы выбранного языка")
            continue

        # начальные координаты и направление
        while True:
            start_row = input("введите номер строки (0-4): ")
            try:
                start_row = int(start_row)  
            except ValueError:
                print("ошибка: номер строки должен быть числом")
                continue  
            if start_row < 0 or start_row > 4:
                print("ошибка: номер строки должен быть от 0 до 4")
            else: 
                break
        while True:
            start_col = input("введите номер столбца (0-4): ")
            try:
                start_col = int(start_col)  
            except ValueError:
                print("ошибка: номер столбца должен быть числом")
                continue  
            if start_col < 0 or start_col > 4:
                print("ошибка: номер столбца должен быть от 0 до 4")
            else: 
                break
        while True:
            direction = input("введите направление ('h'/'г' для горизонтального, 'v'/'в' для вертикального): ").lower()
            if direction not in ['h', 'v', 'г', 'в']:
                print("ошибка: введите 'h'/'г' для горизонтального или 'v'/'в' для вертикального направления")
            else:
                break  

        # проверка границ поля
        if (direction == 'h' or direction == 'г') and start_col + len(word) > 5:
            print("ошибка: слово не помещается по горизонтали")
            continue
        if (direction == 'v' or direction == 'в') and start_row + len(word) > 5:
            print("ошибка: слово не помещается по вертикали")
            continue

        # проверка на перезапись букв
        if not can_place(word, start_row, start_col, direction):
            print("ошибка: нельзя перезаписать уже существующие буквы")
            continue

        # считаем очки за слово с учетом бонусов
        score = calc(word, language, start_row, start_col, direction)
        total_score += score

        # размещаем слово на поле
        place_on_board(word, start_row, start_col, direction)

        print(f"\n Стоимость слова '{word}' составляет: {score} очков. общий счет: {total_score}")

    print(f"Игра окончена. итоговый счет: {total_score}")

play_game()