import pygame
import sys
import generator

# Инициализация Pygame
pygame.init()

# Определение размеров экрана
screen_width = 400
screen_height = 450
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze Game")

# Определение цветов
white = (255, 255, 255)
black = (0, 0, 0)

bg_main = (173, 214, 255)
button_color = (71, 132, 48)
button_color_active = (204, 255, 0)

clock = pygame.time.Clock()

# Определение шрифта
font = pygame.font.Font(None, 32)

# Определение текстовых элементов меню как кнопок
menu_buttons = []
menu_buttons_paremetrs = []

menu_buttons.append({"text": "Генерация", "rect": pygame.Rect(100, 110, 200, 50)})
menu_buttons_paremetrs.append({"text": "Высота", "rect": pygame.Rect(100, 170, 90, 40)})
menu_buttons_paremetrs.append({"text": "Ширина", "rect": pygame.Rect(210, 170, 90, 40)})
menu_buttons.append({"text": "Загрузить", "rect": pygame.Rect(100, 220, 200, 50)})
menu_buttons.append({"text": "Настройки", "rect": pygame.Rect(100, 280, 200, 50)})
menu_buttons.append({"text": "Выход", "rect": pygame.Rect(100, 340, 200, 50)})

logo = pygame.image.load("logo.png")

# Main Loop

main_window_visible = True
new_game_window_visible = False
input_text = "228"
running  = True
while running:
    if main_window_visible == True:
        pygame.display.update()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in menu_buttons:
                    if button["rect"].collidepoint(event.pos):
                        if button["text"] == "Генерация":
                            new_game_window_visible = True
                            main_window_visible = False  # Закрыть основное окно
                        if button["text"] == "Выход":
                            running = False
        screen.fill(bg_main)

        for button in menu_buttons:
            if button["rect"].collidepoint((mouse_x, mouse_y)):
                pygame.draw.rect(screen, (100, 100, 100), button["rect"])  # Изменение цвета при наведении
            else:
                pygame.draw.rect(screen, button_color, button["rect"])  # Обычный цвет
            text = font.render(button["text"], True, white)
            text_rect = text.get_rect(center=button["rect"].center)
            screen.blit(text, text_rect)

        font = pygame.font.Font(None, 20)

        for button in menu_buttons_paremetrs:
            if button["rect"].collidepoint((mouse_x, mouse_y)):
                pygame.draw.rect(screen, (150, 150, 150), button["rect"])  # Изменение цвета при наведении
            else:
                pygame.draw.rect(screen, button_color, button["rect"])  # Обычный цвет
            text = font.render(button["text"], True, white)
            text_rect = text.get_rect(center=button["rect"].center)
            screen.blit(text, text_rect)
        
        font = pygame.font.Font(None, 32)
        screen.blit(logo, (5, 15))  # Отрисуйте изображение на экране


        pygame.display.flip()
        clock.tick(60) # количество фреймов в секунду
    if new_game_window_visible == True:
        cols = 15
        rows = 15
        type = "dfs"
        maze = generator.generate(cols, rows, type)
        CELL_SIZE = 20
        SCREEN_WIDTH = CELL_SIZE * (cols * 2 + 1) + 10
        SCREEN_HEIGHT = CELL_SIZE * (rows * 2 + 1) + 10
        BG_COLOR = (168, 182, 227)
        WALL_COLOR = (0, 0, 0)
        PLAYER_COLOR = (255, 3, 62)
        START_COLOR = (25, 255, 25)
        END_COLOR = (93, 118, 203)
        PLAYER_X = 1
        PLAYER_Y = 1
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Gen')
        screen.fill(BG_COLOR)
        while new_game_window_visible == True:
            for y, row in enumerate(maze):
                for x, cell in enumerate(row):
                    if cell == " ":
                        pygame.draw.rect(screen, BG_COLOR, (5 + x * CELL_SIZE, 5 + y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    elif cell == "W":
                        pygame.draw.rect(screen, WALL_COLOR, (5 + x * CELL_SIZE, 5 + y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    elif cell == "P" and x == 1 and y == 1:
                        pygame.draw.rect(screen, START_COLOR, (5 + x * CELL_SIZE, 5 + y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        pygame.draw.rect(screen, black, (5 + x * CELL_SIZE + 1, 5 + y * CELL_SIZE + 1, CELL_SIZE - 2, CELL_SIZE - 2))
                        pygame.draw.rect(screen, PLAYER_COLOR, (5 + x * CELL_SIZE + 2, 5 + y * CELL_SIZE + 2, CELL_SIZE - 4, CELL_SIZE - 4))
                    elif cell == "P" and x == rows - 1 and y == cols - 1:
                        pygame.draw.rect(screen, END_COLOR, (5 + x * CELL_SIZE, 5 + y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        pygame.draw.rect(screen, black, (5 + x * CELL_SIZE + 1, 5 + y * CELL_SIZE + 1, CELL_SIZE - 2, CELL_SIZE - 2))
                        pygame.draw.rect(screen, PLAYER_COLOR, (5 + x * CELL_SIZE + 2, 5 + y * CELL_SIZE + 2, CELL_SIZE - 4, CELL_SIZE - 4))
                    elif cell == "S":
                        pygame.draw.rect(screen, START_COLOR, (5 + x * CELL_SIZE, 5 + y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    elif cell == "E":
                        pygame.draw.rect(screen, END_COLOR, (5 + x * CELL_SIZE, 5 + y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    elif cell == "P":
                        pygame.draw.rect(screen, black, (5 + x * CELL_SIZE + 1, 5 + y * CELL_SIZE + 1, CELL_SIZE - 2, CELL_SIZE - 2))
                        pygame.draw.rect(screen, PLAYER_COLOR, (5 + x * CELL_SIZE + 2, 5 + y * CELL_SIZE + 2, CELL_SIZE - 4, CELL_SIZE - 4))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    new_game_window_visible = False
                    main_window_visible = True
                    screen = pygame.display.set_mode((screen_width, screen_height))
                elif event.type == pygame.KEYDOWN: # нажата какая-то клавиша
                    if event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_a or event.key == pygame.K_d:
                        maze[PLAYER_X][PLAYER_Y] = " "
                        if event.key == pygame.K_w and maze[PLAYER_X - 1][PLAYER_Y] != "W":
                            PLAYER_X -= 1
                            # Логика для движения вверх
                        elif event.key == pygame.K_a and maze[PLAYER_X][PLAYER_Y - 1] != "W":
                            PLAYER_Y -= 1
                            # Логика для движения влево
                        elif event.key == pygame.K_s and maze[PLAYER_X + 1][PLAYER_Y] != "W":
                            PLAYER_X += 1
                            # Логика для движения вниз
                        elif event.key == pygame.K_d and maze[PLAYER_X][PLAYER_Y + 1] != "W":
                            PLAYER_Y += 1
                            # Логика для движения вправо
                        maze[1][1] = "S"
                        maze[PLAYER_X][PLAYER_Y] = "P"
                        pygame.display.flip()
                        clock.tick(30) # количество фреймов в секунду
            pygame.display.flip()
            clock.tick(30) # количество фреймов в секунду


# Завершение Pygame
pygame.quit()
sys.exit()