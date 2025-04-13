# Sources For Project Inspiration and Guide Below
# CS50.ai and ChatGPT
# https://www.youtube.com/watch?v=q7hIOKGfaRU
# https://www.youtube.com/watch?v=bwuosv2m70g

import tkinter as tk
import random
import time

# Constant Values that DO NOT Change
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 800
BALL_RADIUS = 20
FPS = 60
BLUE = '#0000FF'
RED = '#FF0000'
WHITE = '#FFFFFF'

# Global Variables for Whole Code Space
game_running = False
ball = None
last_ball_time = time.time()
start_time = time.time()
balls_shown = 0
print("Note: Ball lasts in miliseconds, the higher the number the easier the dificulty and vice vertsa")
ball_appear_time = int(
    input("How long do you want the ball to last (Miliseconds): "))
print("Note: Timer is in seconds")
timer = int(input("How much time do you want? "))
ball_count = timer
game_mode = 'time'

# Functions To Run Game


def start_game():
    global game_running, start_time, last_ball_time, balls_shown
    global ball_appear_time, ball_count, timer, game_mode

    canvas.delete("all")
    points_label.config(text="Points: 0")
    timer_label.config(text=f"Timer: {timer}")
    game_running = True
    start_time = time.time()
    last_ball_time = time.time()
    balls_shown = 0
    root.after(500, show_ball)
    update_timer()


def update_timer():
    global game_running, timer, start_time, game_mode, balls_shown, ball_count

    if game_running:
        elapsed_time = time.time() - start_time
        timer -= 1
        timer_label.config(text=f"Timer: {timer}")
        if timer > 0:
            root.after(1000, update_timer)
        else:
            game_running = False
            end_game()


def show_ball():
    global game_running, last_ball_time, ball_appear_time, balls_shown

    if game_running:
        if time.time() - last_ball_time >= ball_appear_time / 1000:
            canvas.delete("ball")
            color = BLUE if random.choice([True, False]) else RED
            x = random.randint(BALL_RADIUS, WINDOW_WIDTH - BALL_RADIUS)
            y = random.randint(BALL_RADIUS, WINDOW_HEIGHT - BALL_RADIUS)
            global ball
            ball = canvas.create_oval(x - BALL_RADIUS, y - BALL_RADIUS, x +
                                      BALL_RADIUS, y + BALL_RADIUS, fill=color,
                                      outline="", tags="ball")
            canvas.tag_bind(ball, "<Button-1>", hit_ball)
            last_ball_time = time.time()
            balls_shown += 1
        root.after(50, show_ball)


def hit_ball(event):
    global game_running, balls_shown

    if game_running:
        canvas.delete("ball")
        points = int(points_label.cget("text").split(": ")[1]) + 2
        points_label.config(text=f"Points: {points}")
        balls_shown += 1
        last_ball_time = time.time()
        show_ball()


def end_game():
    global game_running
    game_running = False
    canvas.delete("all")
    timer_label.config(text="Game Over!")
    final_points = points_label.cget("text").split(": ")[1]
    points_label.config(text=f"Final Points: {final_points}")


root = tk.Tk()
root.title("Welcome to Makeshift Aim Trainer")
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=WHITE)
canvas.pack()

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack()

timer_label = tk.Label(root, text=f"Timer: {str(timer)}")
timer_label.pack()

points_label = tk.Label(root, text="Points: 0")
points_label.pack()

root.mainloop()
