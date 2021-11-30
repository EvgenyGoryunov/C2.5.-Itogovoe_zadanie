from random import randint

field = [[" "] * 7 for a in range(7)]


def show():
    print("___|_1_|_2_|_3_|_4_|_5_|_6_|")  # печать верхней, первой строчки поля
    for q in range(1, 7):
        print(f" {q} | {field[q][1]} | {field[q][2]} | {field[q][3]} | {field[q][4]} | {field[q][5]} | {field[q][6]} |")


class Ship:
    def __init__(self, shipLenght):
        self.shipLenght = shipLenght
        self.x = randint(1, 6)
        self.y = randint(1, 6)
        self.shipOrient = randint(0, 1)


l = [3, 2, 2, 1, 1, 1, 1]

p = 0
t = 0
for i in l:
    t += 1
    while True:
        p += 1
        qaz = Ship(i)
        if qaz.x + i - 1 < 7 and qaz.y + i - 1 < 7 and field[qaz.x][qaz.y] == " ":
            print(f'\n{p}) voshlo')
            for w in range(i):
                    if qaz.shipOrient == 1:
                        print(f'x:{qaz.x + w}, y:{qaz.y}, vert')
                        field[qaz.x + w][qaz.y] = t #"■"
                    else:
                        print(f'x:{qaz.x}, y:{qaz.y + w}, gorizont')
                        field[qaz.x][qaz.y + w] = t #"■"
            show()
            break

        else:
            print(f'\n{p}) ne voshlo')
            print(f'x:{qaz.x}, y:{qaz.y}, l:{i}')
            continue

# нужно добавить мертвые зоны вокруг корабля
# переписать условия на основе вызова исключений
