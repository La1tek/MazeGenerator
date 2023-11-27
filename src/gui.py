import os
import sys

import pygame

import generator
import utils


# Инициализация Pygame
pygame.init()

# Определение размеров экрана
screen_width = 400
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze Game | By @La1tek")

# Определение цветов
white = (255, 255, 255)
black = (0, 0, 0)

bg_main = (173, 214, 255)
button_color = (71, 132, 48)
button_color_active = (124, 175, 5) # (204, 255, 0)
text_color = (0, 152, 0)

BG_COLOR = (0, 102, 51)
WALL_COLOR = (0, 0, 0)
PLAYER_COLOR = (255, 3, 62)
START_COLOR = BG_COLOR  #(25, 255, 25)
END_COLOR = (93, 118, 203)

clock = pygame.time.Clock()

# Определение шрифта
font = pygame.font.Font(None, 32)

# Определение текстовых элементов меню как кнопок
menu_buttons = []
widht_buttons = []
height_buttons = []
type_buttons = []
menu_buttons.append({"text": "Генерация", "rect": pygame.Rect(100, 120, 200, 50)}) 
widht_buttons.append({"text": "0", "rect": pygame.Rect(100, 180, 20, 40)})
widht_buttons.append({"text": "Wight", "rect": pygame.Rect(130, 180, 30, 40)})
widht_buttons.append({"text": "1", "rect": pygame.Rect(170, 180, 20, 40)})
height_buttons.append({"text": "0", "rect": pygame.Rect(210, 180, 20, 40)})
height_buttons.append({"text": "Height", "rect": pygame.Rect(240, 180, 30, 40)})
height_buttons.append({"text": "1", "rect": pygame.Rect(280, 180, 20, 40)})
type_buttons.append({"text": "0", "rect": pygame.Rect(100, 240, 20, 40)})
type_buttons.append({"text": "Type", "rect": pygame.Rect(130, 240, 140, 40)})
type_buttons.append({"text": "1", "rect": pygame.Rect(280, 240, 20, 40)})
menu_buttons.append({"text": "Загрузить", "rect": pygame.Rect(140, 290, 120, 50)})
menu_buttons.append({"text": "Настройки", "rect": pygame.Rect(100, 350, 200, 50)})
menu_buttons.append({"text": "Выход", "rect": pygame.Rect(145, 410, 110, 50)})


logo = pygame.image.load("src/Sprites/logo.png")
player = pygame.image.load("src/Sprites/player.png")
bg = pygame.image.load("src/Sprites/bg_blur.jpg")
bg_play = pygame.image.load("src/Sprites/bg_play.png")

pygame.mixer.music.load("src/other/bg_sound.mp3")
pygame.mixer.music.play(0)
pygame.mixer.music.set_volume(0.1)

digits = [
    pygame.image.load("src/Sprites/Digits/5.png"),
    pygame.image.load("src/Sprites/Digits/6.png"),
    pygame.image.load("src/Sprites/Digits/7.png"),
    pygame.image.load("src/Sprites/Digits/8.png"),
    pygame.image.load("src/Sprites/Digits/9.png"),
    pygame.image.load("src/Sprites/Digits/10.png"),
    pygame.image.load("src/Sprites/Digits/11.png"),
    pygame.image.load("src/Sprites/Digits/12.png"),
    pygame.image.load("src/Sprites/Digits/13.png"),
    pygame.image.load("src/Sprites/Digits/14.png"),
    pygame.image.load("src/Sprites/Digits/15.png"),
]

arrows = [
    [pygame.image.load("src/Sprites/Arrows/left_arrow.png"),
    pygame.image.load("src/Sprites/Arrows/right_arrow.png")],
    [pygame.image.load("src/Sprites/Arrows/left_arrow_act.png"),
    pygame.image.load("src/Sprites/Arrows/right_arrow_act.png")],
    [pygame.image.load("src/Sprites/Arrows/larrow.png"),
    pygame.image.load("src/Sprites/Arrows/rarrow.png")]
]

type_gen = [
    pygame.image.load("src/Sprites/mst.png"),
    pygame.image.load("src/Sprites/dfs.png")
]

title_menu = [
    pygame.image.load("src/Sprites/Titles/gen.png"),
    pygame.image.load("src/Sprites/Titles/gen_act.png"),
    pygame.image.load("src/Sprites/Titles/load.png"),
    pygame.image.load("src/Sprites/Titles/load_act.png"),
    pygame.image.load("src/Sprites/Titles/load_block.png"),
    pygame.image.load("src/Sprites/Titles/exit.png"),
    pygame.image.load("src/Sprites/Titles/exit_act.png")
]

# Main Loop

CELL_SIZE = 25
BUTTON_SAVE_HEIGHT = 50

cols = 10
rows = 10
type = 0 # 1 - dfs, 0 - mst
types = ["DFS","MST"]

main_window_visible = True
new_game_window_visible = False

running  = True
while running:
    if main_window_visible == True:
        screen.blit(bg, (0, 0))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in menu_buttons:
                    if button["rect"].collidepoint(event.pos):
                        if button["text"] == "Генерация":
                            load = False
                            new_game_window_visible = True
                            main_window_visible = False  # Закрыть основное окно
                        if button["text"] == "Выход":
                            running = False
                        if button["text"] == "Загрузить" and len(os.listdir(os.getcwd() + "/src/Loader")) != 0:
                            load = True
                            new_game_window_visible = True
                            main_window_visible = False
                for button in widht_buttons:
                    if button["rect"].collidepoint(event.pos):
                        if button["text"] == "0" and cols > 5:
                            cols -= 1
                        if button["text"] == "1" and cols < 15:
                            cols += 1
                for button in height_buttons:
                    if button["rect"].collidepoint(event.pos):
                        if button["text"] == "0" and rows > 5:
                            rows -= 1
                        if button["text"] == "1" and rows < 15:
                            rows += 1
                for button in type_buttons:
                    if button["rect"].collidepoint(event.pos) and button["text"] != "Type":
                        type = 1 - type

        for button in menu_buttons:
            if button["text"] == "Генерация":
                if button["rect"].collidepoint((mouse_x, mouse_y)):
                    image = title_menu[1] # Изменение цвета при наведении
                else:
                    image = title_menu[0]  # Обычный цвет
                image_rect = image.get_rect(center=button["rect"].center)
                screen.blit(image, image_rect)

            elif button["text"] == "Загрузить":
                if not os.path.exists("src/Loader"):
                    os.makedirs("src/Loader")
                if button["rect"].collidepoint((mouse_x, mouse_y)):
                    if len(os.listdir(os.getcwd() + "/src/Loader")) != 0:
                        image = title_menu[3] # Изменение цвета при наведении
                    else:
                        image = title_menu[4]
                else:
                    image = title_menu[2]  # Обычный цвет
                image_rect = image.get_rect(center=button["rect"].center)
                screen.blit(image, image_rect)
            elif button["text"] == "Выход":
                if button["rect"].collidepoint((mouse_x, mouse_y)):
                    image = title_menu[6] # Изменение цвета при наведении
                else:
                    image = title_menu[5]  # Обычный цвет
                image_rect = image.get_rect(center=button["rect"].center)
                screen.blit(image, image_rect)
        

        for button in widht_buttons:
            if button["text"] == "Wight":
                text_rect = digits[cols - 5].get_rect(center=button["rect"].center)
                screen.blit(digits[cols - 5], text_rect)
            elif button["text"] == "0" and cols > 5:
                if button["rect"].collidepoint((mouse_x, mouse_y)):
                    image = arrows[1][int(button["text"])] # Изменение цвета при наведении
                else:
                    image = arrows[0][int(button["text"])]  # Обычный цвет
                image_rect = image.get_rect(center=button["rect"].center)
                screen.blit(image, image_rect)
            elif button["text"] == "1" and cols < 15:
                if button["rect"].collidepoint((mouse_x, mouse_y)):
                    image = arrows[1][int(button["text"])] # Изменение цвета при наведении
                else:
                    image = arrows[0][int(button["text"])]  # Обычный цвет
                image_rect = image.get_rect(center=button["rect"].center)
                screen.blit(image, image_rect)
            

        
        for button in height_buttons:
            if button["text"] == "Height":
                text_rect = digits[rows - 5].get_rect(center=button["rect"].center)
                screen.blit(digits[rows - 5], text_rect)
            elif button["text"] == "0" and rows > 5:
                if button["rect"].collidepoint((mouse_x, mouse_y)):
                    image = arrows[1][int(button["text"])] # Изменение цвета при наведении
                else:
                    image = arrows[0][int(button["text"])]  # Обычный цвет
                image_rect = image.get_rect(center=button["rect"].center)
                screen.blit(image, image_rect)
            elif button["text"] == "1" and rows < 15:
                if button["rect"].collidepoint((mouse_x, mouse_y)):
                    image = arrows[1][int(button["text"])] # Изменение цвета при наведении
                else:
                    image = arrows[0][int(button["text"])]  # Обычный цвет
                image_rect = image.get_rect(center=button["rect"].center)
                screen.blit(image, image_rect)

        for button in type_buttons:
            if button["text"] != "Type":
                if button["rect"].collidepoint((mouse_x, mouse_y)):
                    image = arrows[2][int(button["text"])] # Изменение цвета при наведении
                else:
                    image = arrows[2][int(button["text"])]  # Обычный цвет
                image_rect = image.get_rect(center=button["rect"].center)
                screen.blit(image, image_rect)
            else:
                image = type_gen[type]
                image_rect = image.get_rect(center=button["rect"].center)
                screen.blit(image, image_rect)

        screen.blit(logo, (5, 15))  # Отрисуйте изображение на экране

        pygame.display.flip()
        clock.tick(60) # количество фреймов в секунду

    if new_game_window_visible == True:
        if not(load):
            maze = generator.generate(cols, rows, types[type])
        else:
            inf = utils.load()
            maze = inf[0]
            cols = inf[1]
            rows = inf[2]
        load = False
        SCREEN_WIDTH = CELL_SIZE * (cols * 2 + 1)
        SCREEN_HEIGHT = CELL_SIZE * (rows * 2 + 1) + BUTTON_SAVE_HEIGHT
        PLAYER_X = 1
        PLAYER_Y = 1
        win = False
        save_button = []
        save_button.append({"text": "Сохранить", "rect": pygame.Rect(0, SCREEN_HEIGHT - BUTTON_SAVE_HEIGHT, SCREEN_WIDTH, BUTTON_SAVE_HEIGHT)})
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.fill(BG_COLOR)
        restart = False
        while new_game_window_visible == True:
            maze[PLAYER_X][PLAYER_Y] = "P"
            maze[2 * rows - 1][2 * cols - 1] = "E"
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for y, row in enumerate(maze):
                for x, cell in enumerate(row):
                    if cell == "0":
                        pygame.draw.rect(screen, BG_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    elif cell == "1":
                        pygame.draw.rect(screen, WALL_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    elif cell == "P" and y == 2 * rows - 1 and x == 2 * cols - 1:
                        pygame.draw.rect(screen, END_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        pygame.draw.rect(screen, black, (x * CELL_SIZE + 1, y * CELL_SIZE + 1, CELL_SIZE - 2, CELL_SIZE - 2))
                        pygame.draw.rect(screen, PLAYER_COLOR, (x * CELL_SIZE + 2, y * CELL_SIZE + 2, CELL_SIZE - 4, CELL_SIZE - 4))
                    elif cell == "E":
                        pygame.draw.rect(screen, black, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        pygame.draw.rect(screen, END_COLOR, (x * CELL_SIZE + 1, y * CELL_SIZE + 1, CELL_SIZE - 2, CELL_SIZE - 2))
                    elif cell == "P":
                        pygame.draw.rect(screen, black, (x * CELL_SIZE + 1, y * CELL_SIZE + 1, CELL_SIZE - 2, CELL_SIZE - 2))
                        pygame.draw.rect(screen, PLAYER_COLOR, (x * CELL_SIZE + 2, y * CELL_SIZE + 2, CELL_SIZE - 4, CELL_SIZE - 4))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    new_game_window_visible = False
                    main_window_visible = True
                    screen = pygame.display.set_mode((screen_width, screen_height))
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for button in save_button:
                        if button["rect"].collidepoint(event.pos):
                            if button["text"] == "Сохранить":
                                utils.save(maze, rows, cols)
                elif event.type == pygame.KEYDOWN: # нажата какая-то клавиша
                    if not(win):
                        if event.key == pygame.K_p:
                            restart = True
                        if event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_a or event.key == pygame.K_d:
                            maze[PLAYER_X][PLAYER_Y] = "0"
                            if event.key == pygame.K_w and maze[PLAYER_X - 1][PLAYER_Y] != "1":
                                PLAYER_X -= 1
                                # Логика для движения вверх
                            elif event.key == pygame.K_a and maze[PLAYER_X][PLAYER_Y - 1] != "1":
                                PLAYER_Y -= 1
                                # Логика для движения влево
                            elif event.key == pygame.K_s and maze[PLAYER_X + 1][PLAYER_Y] != "1":
                                PLAYER_X += 1
                                # Логика для движения вниз
                            elif event.key == pygame.K_d and maze[PLAYER_X][PLAYER_Y + 1] != "1":
                                PLAYER_Y += 1
                                # Логика для движения вправо
                            maze[PLAYER_X][PLAYER_Y] = "P"
                            if PLAYER_X == 2 * rows - 1 and PLAYER_Y == 2 * cols - 1:
                                win = True
                            pygame.display.flip()
                            clock.tick(120) # количество фреймов в секунду
                    else:
                        if event.key == pygame.K_SPACE:
                            restart = True
            if win:
                font = pygame.font.Font(None, 72)
                text = font.render('YOU WIN', True, white)
                text_rect = text.get_rect(center=pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT - BUTTON_SAVE_HEIGHT).center)
                screen.blit(text, text_rect)
                font = pygame.font.Font(None, 32)
                text = font.render('"Space" to Restart', True, white)
                text_rect = text.get_rect(center=pygame.Rect(0, BUTTON_SAVE_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT - BUTTON_SAVE_HEIGHT).center)
                screen.blit(text, text_rect)
                
            for button in save_button:
                if button["rect"].collidepoint((mouse_x, mouse_y)):
                    pygame.draw.rect(screen, button_color, button["rect"])  # Изменение цвета при наведении
                else:
                    pygame.draw.rect(screen, BG_COLOR, button["rect"])  # Обычный цвет
                text = font.render(button["text"], True, white)
                text_rect = text.get_rect(center=button["rect"].center)
                screen.blit(text, text_rect)
            pygame.display.flip()
            clock.tick(60) # количество фреймов в секунду
            if restart:
                break


# Завершение Pygame
pygame.quit()
sys.exit()

