board = list(range(1, 10)) #Сгенерируем числа от 1 до 9
def draw_board(board): #Создадим функцию
    print("-" * 13) #выводим первую строку из 13 "тире"
    for i in range(3): #в цикле прорисовываем остальные края поля
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13) #выводим последнюю строку из 13 "тире"
def take_input(player_token): #функция для приёма ввода
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except ValueError:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if 1 <= player_answer <= 9:
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")

draw_board(board)