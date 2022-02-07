import math
from datetime import datetime

import pygame
from random import *
from tkinter import *
from tkinter import messagebox


def home_screen():
    title = pygame.image.load("img/title.png")
    start_btn = pygame.image.load("img/start_btn.png")
    rank_btn = pygame.image.load("img/rank_btn.png")
    screen.blit(title, (310, 40))
    screen.blit(start_btn, (480, 430))
    screen.blit(rank_btn, (1150, 603))


def menu_screen():
    global user_text, select_setup

    menu = pygame.image.load("img/menu.png")
    screen.blit(menu, (310, 20))

    text_mode1 = korean.render("자유", True, WHITE)
    text_rule1 = english.render("×1", True, WHITE)
    text_rule2 = english.render("×2", True, WHITE)
    text_rule3 = english.render("×3", True, WHITE)
    text_time = korean.render("무제한", True, WHITE)
    text_record1 = korean.render("사용", True, WHITE)
    text_record2 = korean.render("미사용", True, WHITE)
    start_button = korean.render("게임 시작", True, WHITE)

    if select_setup[0] == 1:
        text_mode1 = korean.render("자유", True, GREEN)
    if select_setup[1] == 1:
        text_rule1 = english.render("×1", True, GREEN)
    elif select_setup[1] == 2:
        text_rule2 = english.render("×2", True, GREEN)
    elif select_setup[1] == 3:
        text_rule3 = english.render("×3", True, GREEN)
    if select_setup[2] == 1:
        text_box = english.render(user_text, True, GREEN)
    elif select_setup[2] == 2:
        text_time = korean.render("무제한", True, GREEN)
    if select_setup[3]:
        text_record1 = korean.render("사용", True, GREEN)
        user_text = "30"
        select_setup[2] = 1
    else:
        text_record2 = korean.render("미사용", True, GREEN)

    screen.blit(text_mode1, (745, 55))
    screen.blit(text_rule1, (600, 185))
    screen.blit(text_rule2, (745, 185))
    screen.blit(text_rule3, (890, 185))
    screen.blit(text_record1, (630, 460))
    screen.blit(text_record2, (830, 460))
    screen.blit(text_time, (830, 325))
    screen.blit(start_button, (550, 600))
    pygame.draw.rect(screen, color, input_rect, 2)
    if user_text == '0' or select_setup[2] == 2:
        text_box = english.render(user_text, True, WHITE)
    else:
        text_box = english.render(user_text, True, GREEN)

    screen.blit(text_box, (input_rect.x + 10, input_rect.y + 15))

    input_rect.w = max(10, text_box.get_width() + 20)
    pygame.display.flip()


def game_screen():
    global total_time
    total_time = select_setup[2]

    for idx, rect in enumerate(game_buttons):
        pygame.draw.rect(screen, RED, rect)


def timeover_screen():
    if select_setup[2] == 2:
        result_score = gameover_font.render(f"GAME OVER", True, WHITE)
        screen.blit(result_score, (400, 200))
        result_time = korean.render(f"총 플레이 시간: {math.floor(elapsed_time - 2)}", True, WHITE)
        screen.blit(result_time, (430, 295))
        result_score = korean.render(f"총 점수: {score}", True, WHITE)
        screen.blit(result_score, (430, 350))
    else:
        result_score = gameover_font.render(f"GAME OVER", True, WHITE)
        screen.blit(result_score, (400, 200))
        result_time = korean.render(f"총 플레이 시간: {select_setup[2]}", True, WHITE)
        screen.blit(result_time, (430, 295))
        result_score = korean.render(f"총 점수: {score}", True, WHITE)
        screen.blit(result_score, (430, 350))

    kr_go_home = korean.render(f"게임 종료하기: ", True, WHITE)
    screen.blit(kr_go_home, (430, 450))
    eng_go_home = english.render(f"Q", True, WHITE)
    screen.blit(eng_go_home, (680, 455))

    if select_setup[3]:
        root.mainloop()


def rank_screen():
    menu = pygame.image.load("img/mode.png")
    screen.blit(menu, (150, 20))
    menu = pygame.image.load("img/rule.png")
    screen.blit(menu, (600, 20))

    text_mode1 = korean.render("자유", True, GREEN)
    text_rule1 = english.render("×1", True, WHITE)
    text_rule2 = english.render("×2", True, WHITE)
    text_rule3 = english.render("×3", True, WHITE)

    if select_rule == 1:
        text_rule1 = english.render("×1", True, GREEN)
    elif select_rule == 2:
        text_rule2 = english.render("×2", True, GREEN)
    elif select_rule == 3:
        text_rule3 = english.render("×3", True, GREEN)

    screen.blit(text_mode1, (400, 20))
    screen.blit(text_rule1, (800, 30))
    screen.blit(text_rule2, (910, 30))
    screen.blit(text_rule3, (1030, 30))

    rank_data = open("rank.txt", "r", encoding="utf-8").readline()
    rank_lists = []
    for rank_list in rank_data.split("@"):
        rank_lists.append(rank_list.split("|"))
    rank_lists = sort_rank(rank_lists)

    cnt = 0

    rank_text0 = english.render("rank", True, WHITE)
    rank_text1 = english.render("nickname", True, WHITE)
    rank_text2 = english.render("score", True, WHITE)
    rank_text3 = english.render("rule", True, WHITE)
    rank_text4 = english.render("date", True, WHITE)

    if len(rank_data) == 0:
        pass
    else:
        if 3 >= select_rule >= 1:
            screen.blit(rank_text0, (150, 100))
            screen.blit(rank_text1, (250, 100))
            screen.blit(rank_text2, (635, 100))
            screen.blit(rank_text4, (900, 100))
            for idx, rank in enumerate(rank_lists):
                if cnt == 11:
                    break
                if int(rank[1]) == select_rule:

                    rank_text0 = english.render(f"{cnt+1}", True, WHITE)
                    screen.blit(rank_text0, (150, 150 + 50 * cnt))
                    rank_text1 = english.render(rank[0], True, WHITE)
                    screen.blit(rank_text1, (250, 150 + 50 * cnt))
                    rank_text2 = english.render(rank[2], True, WHITE)
                    screen.blit(rank_text2, (650, 150 + 50 * cnt))
                    rank_text3 = english.render(rank[3], True, WHITE)
                    screen.blit(rank_text3, (850, 150 + 50 * cnt))

                    cnt += 1
        else:
            screen.blit(rank_text0, (150, 100))
            screen.blit(rank_text1, (250, 100))
            screen.blit(rank_text2, (535, 100))
            screen.blit(rank_text3, (740, 100))
            screen.blit(rank_text4, (900, 100))

            for idx, rank in enumerate(rank_lists):
                if idx == 11:
                    break
                rank_text0 = english.render(f"{idx+1}", True, WHITE)
                screen.blit(rank_text0, (150, 150 + 50 * idx))
                rank_text1 = english.render(rank[0], True, WHITE)
                screen.blit(rank_text1, (250, 150 + 50 * idx))
                rank_text2 = english.render(rank[2], True, WHITE)
                screen.blit(rank_text2, (550, 150 + 50 * idx))
                rank_text3 = english.render(f"×{rank[1]}", True, WHITE)
                screen.blit(rank_text3, (750, 150 + 50 * idx))
                rank_text4 = english.render(rank[3], True, WHITE)
                screen.blit(rank_text4, (850, 150 + 50 * idx))

    pygame.display.flip()


def save():
    read = open("rank.txt", "r", encoding="utf-8").readline()
    save = open("rank.txt", "a", encoding="utf-8")

    if len(read) == 0:
        save.write(f"{nickname.get()}|{select_setup[1]}|{score}|{datetime.today().strftime('%Y/%m/%d')}")
    else:
        save.write(f"@{nickname.get()}|{select_setup[1]}|{score}|{datetime.today().strftime('%Y/%m/%d')}")
    save.close()

    root.destroy()


def shuffle_grid(number_count):
    rows = 34
    columns = 62

    cell_size = 20  # 각 Grid cell 별 가로, 세로 크기  1280
    button_size = 20  # Grid cell 내에 실제로 그려질 버튼 크기 720
    screen_left_margin = 20  # 전체 스크린 왼쪽 여백
    screen_top_margin = 20  # 전체 스크린 위쪽 여백

    grid = [[0 for col in range(columns)] for row in range(rows)]

    number = 1  # 시작 숫자 1부터 number_count 까지, 만약 5라면 5까지 숫자를 랜덤으로 배치하기
    while number <= number_count:
        row_idx = randrange(0, rows)  # 0, 1, 2, 3, 4 중에서 랜덤으로 뽑기
        col_idx = randrange(0, columns)  # 0 ~ 8 중에서 랜덤으로 뽑기

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = 1  # 숫자 지정
            number += 1

            # 현재 grid cell 위치 기준으로 x, y 위치를 구함
            center_x = screen_left_margin + (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) + (cell_size / 2)

            # 숫자 버튼 만들기
            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)

            game_buttons.append(button)

    # 배치된 랜덤 숫자 확인
    # print(grid)


def sort_rank(rank_list):
    for i in range(len(rank_list) - 1):
        for j in range(len(rank_list) - i - 1):
            if int(rank_list[j][2]) < int(rank_list[j + 1][2]):
                rank_list[j], rank_list[j + 1] = rank_list[j + 1], rank_list[j]

    return rank_list


def check_buttons(pos):
    global start, active, user_text, start_ticks, time_type, select_rule
    if start == 0:
        if start_button.collidepoint(pos):
            start = 1
        elif rank_button.collidepoint(pos):
            start = 4
    elif start == 1:
        if input_rect.collidepoint(pos):
            active = True
            select_setup[2] = 1
        else:
            active = False
        if mode1.collidepoint(pos):
            select_setup[0] = 1
        if rule1.collidepoint(pos):
            select_setup[1] = 1
        elif rule2.collidepoint(pos):
            select_setup[1] = 2
        elif rule3.collidepoint(pos):
            select_setup[1] = 3
        if time2.collidepoint(pos):
            select_setup[2] = 2
        if record1.collidepoint(pos):
            select_setup[3] = True
            user_text = "30"
        elif record2.collidepoint(pos):
            select_setup[3] = False
        if start_btn.collidepoint(pos):
            time_type = 2
            start_ticks = pygame.time.get_ticks()
            if select_setup[2] == 1:
                select_setup[2] = int(user_text)
                setup = select_setup
                time_type = 1
            start = 2
            shuffle_grid(select_setup[1])
    elif start == 2:
        check_game_button(pos)
    elif start == 3:
        pass
    elif start == 4:
        if rule_1.collidepoint(pos):
            if select_rule == 1:
                select_rule = 0
            else:
                select_rule = 1
        elif rule_2.collidepoint(pos):
            if select_rule == 2:
                select_rule = 0
            else:
                select_rule = 2
        elif rule_3.collidepoint(pos):
            if select_rule == 3:
                select_rule = 0
            else:
                select_rule = 3


def check_game_button(pos):
    global score
    for idx, button in enumerate(game_buttons):
        if button.collidepoint(pos):
            del game_buttons[idx]
            score += 10

    if len(game_buttons) == 0:
        shuffle_grid(select_setup[1])


BLACK = (0, 0, 0)  # RGB
WHITE = (255, 255, 255)
GREEN = (0, 255, 25)
GRAY = (50, 50, 50)
RED = (255, 0, 0)

pygame.init()
pygame.font.init()
screen_width = 1280  # 가로 크기
screen_height = 720  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Aim Game")
gameover_font = pygame.font.Font("font/BOKEH.ttf", 100)
english = pygame.font.Font("font/BOKEH.ttf", 50)  # 보케체, greenegg, 공유마당
my_score = pygame.font.Font("font/BOKEH.ttf", 20)  # 보케체, greenegg, 공유마당
korean = pygame.font.Font("font/KoPubWorld Dotum Bold.ttf", 40)  # Kopub World 돋움체 B, 문화체육관광부, 공유마당

# 메인
start_button = pygame.Rect(0, 0, 300, 105)
start_button.center = (629, 477)
rank_button = pygame.Rect(0, 0, 100, 100)
rank_button.center = (1200, 650)

# 메뉴
user_text = '0'
input_rect = pygame.Rect(630, 325, 100, 70)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('gray15')
color = color_passive
select_setup = [1, 2, 2, False]
mode1 = pygame.Rect(0, 0, 66, 45)
rule1 = pygame.Rect(0, 0, 40, 45)
rule2 = pygame.Rect(0, 0, 40, 45)
rule3 = pygame.Rect(0, 0, 40, 45)
time2 = pygame.Rect(0, 0, 100, 45)
record1 = pygame.Rect(0, 0, 66, 45)
record2 = pygame.Rect(0, 0, 100, 45)
mode1.center = (781, 80)
rule1.center = (614, 206)
rule2.center = (767, 206)
rule3.center = (912, 206)
time2.center = (884, 354)
record1.center = (666, 490)
record2.center = (884, 490)

# 게임
start_ticks = None
total_time = None
start_btn = pygame.Rect(0, 0, 240, 45)
start_btn.center = (620, 625)
game_buttons = []

# 결과
root = Tk()
root.title("점수 저장")
root.geometry("300x50")
root.resizable(0, 0)

lbl = Label(root, text="nickname(영어로 입력해주세요)", font="NanumGothic 10")
lbl.grid(row=0, column=1)

nickname = Entry(root)
nickname.grid(row=1, column=0)

btn1 = Button(root, text="save", command=save, width=6, height=1)
btn1.grid(row=1, column=1)

# 랭킹
select_rule = 0
rule_1 = pygame.Rect(0, 0, 40, 45)
rule_2 = pygame.Rect(0, 0, 40, 45)
rule_3 = pygame.Rect(0, 0, 40, 45)
rule_1.center = (815, 50)
rule_2.center = (935, 50)
rule_3.center = (1055, 50)


active = False
start = 0
time_type = 2
running = True
score = 0
elapsed_time = None

while running:
    screen.fill(BLACK)
    click_pos = None

    # 이벤트 루프
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # db.close()
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()

        if event.type == pygame.KEYDOWN:
            if start == 1:
                if event.key == pygame.K_ESCAPE:
                    start = 0
            if start == 2:
                if event.key == pygame.K_ESCAPE:
                    start = 3
            if start == 3:
                if event.key == pygame.K_q:
                    # db.close()
                    running = False
            if start == 4:
                if event.key == pygame.K_ESCAPE:
                    start = 0
            if active:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
    if active:
        color = color_active
    else:
        color = color_passive

    if click_pos:
        check_buttons(click_pos)
    if start == 1:  # 선택
        menu_screen()
    elif start == 2:  # 게임
        game_screen()
        if total_time is not None and time_type == 1:
            elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
            timer = english.render("timer: " + str(int(total_time - elapsed_time) + 1), True, WHITE)
            scorer = english.render("score: " + str(score), True, WHITE)
            screen.blit(timer, (10, 10))
            screen.blit(scorer, (10, 55))

            if total_time - elapsed_time <= 0:
                start = 3
        elif total_time is not None and time_type == 2:
            text = korean.render("나가기: ", True, WHITE)
            screen.blit(text, (10, 645))
            text = english.render("ESC", True, WHITE)
            screen.blit(text, (130, 654))
            elapsed_time = pygame.time.get_ticks() / 1000
            timer = english.render("time: " + str(int(elapsed_time) - 2), True, WHITE)
            scorer = english.render("score: " + str(score), True, WHITE)
            screen.blit(timer, (10, 10))
            screen.blit(scorer, (10, 55))
        pygame.display.flip()

    elif start == 3:  # 결과
        timeover_screen()
    elif start == 4:  # 랭킹
        rank_screen()
    else:
        home_screen()

    pygame.display.update()
pygame.quit()
