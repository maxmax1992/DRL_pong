import numpy as np
import time

WIDTH = 100
HEIGHT = 20
tick_time = 0.030

paddle_height = 4
self_y = (HEIGHT//2, HEIGHT//2+paddle_height)
opp_y = (HEIGHT//2, HEIGHT//2+paddle_height)


def printraw(x): return print(x, end='')


b_coord = (WIDTH//2, HEIGHT//2)
b_dir = np.random.uniform(0, 2*np.pi)
b_speed = 50


def drawWorld():
    str_ = ""
    for i in range(0, HEIGHT):
        for j in range(0, WIDTH):
            if b_coord[0]//1 == j and b_coord[1]//1 == i:
                str_ += '*'
            elif j == 0 and self_y[0] < i and self_y[1] > i:
                str_ += '◼'
            elif j == WIDTH - 1 and opp_y[0] < i and opp_y[1] > i:
                str_ += '◼'
            elif j == WIDTH -1 or j == 0:
                str_ += '-'
            else:
                str_ += '_'
        str_ += '\n'
    print(str_)


def step(tick=tick_time):
    global b_coord
    b_delta_x = np.cos(b_dir)
    b_delta_y = np.sin(b_dir)
    b_coord = b_coord[0] + b_delta_x*tick, b_coord[1] + b_delta_y*tick


while(True):
    drawWorld()
    step()
    time.sleep(tick_time)
