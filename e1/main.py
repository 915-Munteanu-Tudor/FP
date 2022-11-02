import random
import numpy as np

game_matrix = []

def add_snake(dim):
    snake_body=[]

    game_matrix[dim // 2][dim // 2] = '+'
    snake_body.append((dim // 2,dim // 2))

    game_matrix[dim // 2 + 1][dim // 2] = '+'
    snake_body.append((dim // 2 + 1,dim // 2))

    game_matrix[dim // 2 - 1][dim // 2] = '*'
    snake_head = (dim // 2 - 1, dim // 2)

    return snake_head, snake_body

def check_apple(apple_x,apple_y,dim):
    if game_matrix[apple_x][apple_y]!=' ':
        return False
    if apple_x != 0:
        if game_matrix[apple_x - 1][apple_y] == '.':
            return False
    if apple_x != dim-1:
        if game_matrix[apple_x+1][apple_y] == '.':
            return False
    if apple_y != 0:
        if game_matrix[apple_x][apple_y-1] == '.':
            return False
    if apple_y != dim - 1:
        if game_matrix[apple_x][apple_y+1] == '.':
            return False

    return True

def add_apple(dim):
    count = 0
    while True:
        apple_x = random.randint(0,dim-1)
        apple_y = random.randint(0,dim-1)
        count += 1
        if check_apple(apple_x,apple_y,dim):
            game_matrix[apple_x][apple_y] = '.'
            return
        if count > dim**3:
            break

    #case for large number of apples and low number of slots for said apples
    for i in range(dim):
        for j in range(dim):
            if check_apple(i,j,dim):
                game_matrix[apple_x][apple_y] = '.'
                return

    print("A new apple couldn't be added due to lack of space on the board. ")



def initialize_board(dim,apple_count):
    for i in range(dim):
        line = []
        for _ in range(dim):
            line.append(' ')
        game_matrix.append(line)

    snake_head, snake_body = add_snake(dim)
    for i in range(apple_count):
        add_apple(dim)
    return snake_head, snake_body

def print_separator_line(dim):
    for i in range(dim):
        print('+---',end = '')
    print('+')

def view_board(dim):
    for line in game_matrix:
        print_separator_line(dim)
        print('|',end = '')
        for x in line:
            print('',x, '|',end='')
        print('')
    print_separator_line(dim)


def play(dim,snake_head, snake_body,direction = (-1,0)):
    while True:
        movement = 0
        old_direction = direction
        tail = tuple(snake_body[-1])
        command = input("Command: ")
        if command == 'up':
            direction = (-1,0)
        elif command == 'down':
            direction = (1,0)
        elif command == 'left':
            direction = (0,-1)
        elif command == 'right':
            direction = (0,1)
        elif command.startswith("move"):
            params = command.split(" ")
            if len(params) == 1:
                movement = 1
            else:
                movement = int(params[-1])

        if direction != old_direction:
            movement += 1
            if direction[0] == -old_direction[0] or direction[1] == -old_direction[1]:
                print("Can't turn 180 degrees. Input another command. ")
                continue

        while movement > 0:
            apple_eaten = 0
            old_head = snake_head
            tail = tuple(snake_body[-1])
            snake_head = tuple(np.add(snake_head,direction))

            if snake_head[0] < 0 or snake_head[0]>dim-1 or snake_head[1]<0 or snake_head[1]>dim-1:
                return
            if game_matrix[snake_head[0]][snake_head[1]] == '+' and snake_head != tail:
                return
            if game_matrix[snake_head[0]][snake_head[1]] == '.':
                apple_eaten  += 1




            aux = snake_body[0]
            for i in range(len(snake_body)-1,0,-1):
                snake_body[i] = snake_body[i-1]
            game_matrix[tail[0]][tail[1]] = ' '
            game_matrix[snake_head[0]][snake_head[1]] = '*'
            snake_body[0] = old_head
            game_matrix[snake_body[0][0]][snake_body[0][1]] = '+'
            if apple_eaten >0:
                game_matrix[tail[0]][tail[1]] = '+'
                snake_body.append(tail)
                add_apple(dim)

            movement -= 1
        view_board(dim)

def load_settings(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
        line0 = lines[0]
        l = line0.split("=")
        dim = l[-1]
        line1 = lines[1].strip()
        l = line1.split("=")
        apple_count = l[-1]
        return int(dim),int(apple_count)



def main():
    dim,apple_count = load_settings('settings.txt')
    snake_head, snake_body = initialize_board(dim,apple_count)
    view_board(dim)
    play(dim,snake_head,snake_body)
    print("Game over.")

main()
