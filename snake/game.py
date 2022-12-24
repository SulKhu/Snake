import pygame
import random

# initialize the starting screen
pygame.init()

# set starting size of screen
min_x = 0
max_x = 1290
min_y = 0
max_y = 750

screen = pygame.display.set_mode([max_x, max_y])
pygame.display.set_caption("snake")

# start with game running
run = True
vel = 5
x = 30
y = 30
colors = [(0, 0, 255), (255, 0, 0), (27, 94, 62)]
current_color = 0

# set starting variables
move_left = False
move_right = True
move_up = False
move_down = False
size = 30
counter = 0

prev_move = "move_right"
current = "move_right"

# make the screen white
screen.fill((20,20,20))


# stores the position of each segment of the snake
segments = [[x, y], [x-size, y], [x - (size * 2), y], [x - (size * 3), y]]

for segment in segments:
    pygame.draw.rect(screen, colors[current_color], (segment[0], segment[1], size, size))

apple = [(((random.randint(0, max_x - size)) // 30) * 30), ((random.randint(0, max_y - size) // 30) * 30)]

pygame.draw.rect(screen, (255, 0, 0), (apple[0], apple[1], size, size))


# while we are still playing the game
while run:
    pygame.time.delay(75)
    counter += 1
    
    # closing screen end game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print("end")

    keys = pygame.key.get_pressed()

    # if pressed left, move left
    if keys[pygame.K_LEFT]:
        prev_move = current
        current = "move_left"
        move_left = True
        move_right = False
        move_up = False
        move_down = False

    # if pressed right, move right
    if keys[pygame.K_RIGHT]:
        prev_move = current
        current = "move_right"
        move_left = False
        move_right = True
        move_up = False
        move_down = False


    # if pressed up, move up
    if keys[pygame.K_UP]:
        prev_move = current
        current = "move_up"
        move_left = False
        move_right = False
        move_up = True
        move_down = False


    # if pressed down, move down
    if keys[pygame.K_DOWN]:
        prev_move = current
        current = "move_down"
        move_left = False
        move_right = False
        move_up = False
        move_down = True

    # change color if pressed space
    if keys[pygame.K_SPACE]:
        current_color += 1

    if current_color > (len(colors) - 1):
        current_color = 0

    if prev_move == "move_left" and current == "move_right":
        current = "move_left"
        move_left = True
        move_right = False
    
    if prev_move == "move_right" and current == "move_left":
        current = "move_right"
        move_right = True
        move_left = False

    if prev_move == "move_up" and current == "move_down":
        current = "move_up"
        move_up = True
        move_down = False

    if prev_move == "move_down" and current == "move_up":
        current = "move_down"
        move_up = False
        move_down = True

    # print(f"current move : {current} | prev move : {prev_move}")

    # move in correct direction
    if move_left:
        current_move = segments.pop(-1)
        current_move[0] = segments[0][0] - 30
        current_move[1] = segments[0][1]
        segments.insert(0, current_move)
    
    elif move_right:
        current_move = segments.pop(-1)
        current_move[0] = segments[0][0] + 30
        current_move[1] = segments[0][1]
        segments.insert(0, current_move)

    elif move_up:
        current_move = segments.pop(-1)
        current_move[1] = segments[0][1] - 30
        current_move[0] = segments[0][0]
        segments.insert(0, current_move)

    elif move_down:
        current_move = segments.pop(-1)
        current_move[1] = segments[0][1] + 30
        current_move[0] = segments[0][0]
        segments.insert(0, current_move)

    print(current_move)

    # clear screen
    screen.fill((20,20,20))

    

    # if hit edge end game
    if segments[0][0] < min_x or  segments[0][0] >= max_x:
        
        pygame.time.delay(250)
        screen.fill((255, 0, 0))
        pygame.display.flip()
        pygame.time.delay(250)
        print("end")
        pygame.quit()

    if segments[0][1] < min_x or segments[0][1] >= max_y:
        pygame.time.delay(250)
        screen.fill((255, 0, 0))
        pygame.display.flip()
        pygame.time.delay(350)
        print("end")
        pygame.quit()

    for i in range(1, len(segments)):
        if (segments[0][0] == segments[i][0]) and (segments[0][1] == segments[i][1]):
            pygame.time.delay(250)
            screen.fill((255, 0, 0))
            pygame.display.flip()
            pygame.time.delay(350)
            print("end")
            pygame.quit()


    # draw new rectangle
    for segment in segments:
        pygame.draw.rect(screen, colors[current_color], (segment[0], segment[1], size, size))

    pygame.draw.rect(screen, (255, 0, 0), (apple[0], apple[1], size, size))

    # update the screen
    pygame.display.flip()


    if segments[0][0] == apple[0] and segments[0][1] == apple[1]:
        if move_left:
            segments.append([x - size, y])
    
        elif move_right:
            segments.append([x + size, y])

        elif move_up:
            segments.append([x, y + size])

        elif move_down:
            segments.append([x, y - size])

        apple = [(((random.randint(0, max_x - size)) // 30) * 30), ((random.randint(0, max_y - size) // 30) * 30)]

        not_inside = True

        for segment in segments:
            if apple[0] == segment[0] or apple[1] == segment[1]:
                not_inside = False
                continue

        while not not_inside:
            apple = [(((random.randint(0, max_x - size)) // 30) * 30), ((random.randint(0, max_y - size) // 30) * 30)]
            
            inside = False

            for segment in segments:
                if apple[0] == segment[0] or apple[1] == segment[1]:
                    inside = True
                    continue

            if inside == False:
                not_inside = True
            

    
# end game
print("end")
pygame.quit()


