"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel, GOval, GRect
import random

FRAME_RATE = 1         # 100 frames per second
NUM_LIVES = 3			# Number of attempts
up = True





def main():
    graphics = BreakoutGraphics()
    name = random_name()
    num = len(name)
    # text = ''
    text_list = []
    for i in range(num):
        text_list += '—'
    ans_lable = GLabel('ANSWER: '+(' '.join(text_list)))
    ans_lable.font = '-20'
    graphics.window.add(ans_lable, x=0, y=ans_lable.height+10)
    live_lable = GLabel('Lives:')
    live_lable.font = '-20'
    graphics.window.add(live_lable, x=graphics.window.width-155, y=graphics.window.height-5)
    ball_1 = GOval(20, 20, x=graphics.window.width-85, y=graphics.window.height-27)
    ball_1.filled = True
    ball_1.fill_color = 'gray'
    graphics.window.add(ball_1)
    ball_2 = GOval(20, 20, x=graphics.window.width-60, y=graphics.window.height - 27)
    ball_2.filled = True
    ball_2.fill_color = 'gray'
    graphics.window.add(ball_2)
    ball_3 = GOval(20, 20, x=graphics.window.width-35, y=graphics.window.height - 27)
    ball_3.filled = True
    ball_3.fill_color = 'gray'
    graphics.window.add(ball_3)
    global NUM_LIVES
    global up
    # Add the animation loop here!
    # update
    while NUM_LIVES > 0:
        pause(FRAME_RATE)
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        graphics.ball.move(dx=dx, dy=dy)
        graphics.update_words()
        maybe_brick1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)  # the corner of the ball
        maybe_brick2 = graphics.window.get_object_at(graphics.ball.x+2*graphics.ball_r, graphics.ball.y)
        maybe_brick3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+2*graphics.ball_r)
        maybe_brick4 = graphics.window.get_object_at(graphics.ball.x+2*graphics.ball_r, graphics.ball.y+2*graphics.ball_r)
        ball_2r = 2*graphics.ball_r
        ball_right = graphics.ball.x+ball_2r
        ball_bottom = graphics.ball.y+ball_2r
        paddel_r = graphics.paddle.x+graphics.paddle.width
    # check
        for i in range(2):
            for j in range(graphics.paddle.width):
                obj = graphics.window.get_object_at(graphics.paddle.x+j, graphics.paddle.y+i)
                if obj is not None and obj is not graphics.ball and obj is not graphics.paddle:
                    if isinstance(obj, GLabel):
                        # ans += obj.text
                        for k in range(num):
                            ch = name[k]
                            if obj.text == ch:
                                text_list[k] = ch
        ans_lable.text = 'ANSWER: '+(' '.join(text_list))
        if graphics.ball.x <= 0 or ball_right >= graphics.window.width:   # if ball hit the wall
            graphics.set_dx()
        elif graphics.ball.y <= 0:                                                     # if ball hit the top
            graphics.set_dy()
        if maybe_brick1 is not None or maybe_brick2 is not None or maybe_brick3 is not None or maybe_brick4 is not None:
            if ball_bottom >= graphics.paddle.y and graphics.ball.x < paddel_r and ball_right > graphics.paddle.x:
                if up:
                    graphics.set_dy()                                                  # if ball hit the paddle
                    up = False
            if graphics.ball.y < graphics.window.height/2:                             # if ball hit the bricks
                if maybe_brick1 is not None and not isinstance(maybe_brick1, GLabel):
                    bx = maybe_brick1.x
                    by = maybe_brick1.y
                    graphics.window.remove(maybe_brick1)
                    graphics.brick_amount -= 1
                    graphics.set_dy()
                    ch = random_words()
                    graphics.spawn_word(bx+graphics.brick_width/2, by+graphics.brick_hight, ch)
                elif maybe_brick2 is not None and not isinstance(maybe_brick2, GLabel):
                    bx = maybe_brick2.x
                    by = maybe_brick2.y
                    graphics.window.remove(maybe_brick2)
                    graphics.brick_amount -= 1
                    graphics.set_dy()
                    ch = random_words()
                    graphics.spawn_word(bx + graphics.brick_width / 2, by + graphics.brick_hight, ch)
                elif maybe_brick3 is not None and not isinstance(maybe_brick3, GLabel):
                    bx = maybe_brick3.x
                    by = maybe_brick3.y
                    graphics.window.remove(maybe_brick3)
                    graphics.brick_amount -= 1
                    graphics.set_dy()
                    ch = random_words()
                    graphics.spawn_word(bx + graphics.brick_width / 2, by + graphics.brick_hight, ch)
                elif maybe_brick4 is not None and not isinstance(maybe_brick4, GLabel):
                    bx = maybe_brick4.x
                    by = maybe_brick4.y
                    graphics.window.remove(maybe_brick4)
                    graphics.brick_amount -= 1
                    graphics.set_dy()
                    ch = random_words()
                    graphics.spawn_word(bx + graphics.brick_width / 2, by + graphics.brick_hight, ch)
        if graphics.ball.y < graphics.window.height/2:                                 # prevent ball stuck in paddle
            up = True
        if graphics.ball.y > graphics.window.height:                                   # if ball out of the window
            graphics.window.remove(graphics.ball)
            graphics.reset_dx()
            graphics.reset_dy()
            NUM_LIVES -= 1
            if NUM_LIVES == 2:
                graphics.window.remove(ball_3)
            elif NUM_LIVES == 1:
                graphics.window.remove(ball_2)
            elif NUM_LIVES == 0:
                graphics.window.remove(ball_1)
            if NUM_LIVES > 0:
                graphics.window.add(graphics.ball, graphics.window.width/2-graphics.ball_r, graphics.window.height/2-graphics.ball_r)
        if graphics.brick_amount == 0:
            if '—' in text_list:
                black_bg = GRect(graphics.window.width, graphics.window.height + 20, x=0, y=-graphics.window.height)
                black_bg.filled = True
                black_bg.fill_color = 'black'
                graphics.window.add(black_bg)
                while True:
                    black_bg.move(dx=0, dy=20)
                    pause(20)
                    if black_bg.y >= 0:
                        break
                unlucky = GLabel('YOU ARE NOT THE CHOSEN ONE')
                unlucky.font = '-20'
                unlucky.color = 'white'
                graphics.window.add(unlucky, 25, graphics.window.height / 2)
        if (''.join(text_list)) == name:
            win = GLabel('WIN!!')
            win.font = '-45'
            win.color = 'black'
            graphics.window.add(win, (graphics.window.width-win.width)/2, graphics.window.height / 2)
            break
    if NUM_LIVES == 0:
        black_bg = GRect(graphics.window.width, graphics.window.height+20, x=0, y=-graphics.window.height)
        black_bg.filled = True
        black_bg.fill_color = 'black'
        graphics.window.add(black_bg)
        while True:
            black_bg.move(dx=0, dy=20)
            pause(20)
            if black_bg.y >= 0:
                break
        game_over = GLabel('GAME OVER')
        game_over.font = '-45'
        game_over.color = 'white'
        graphics.window.add(game_over, (graphics.window.width-game_over.width)/2, graphics.window.height/2)





def random_words():
    ch = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return ch


def random_name():
    n = random.random()
    if n > 0.7:
        return 'ONEPIECE'
    elif n > 0.5:
        return 'POCKEMON'
    elif n > 0.3:
        return 'NARUTO'
    elif n > 0.1:
        return 'SPYFAMILY'
    else:
        return 'STANCODE'










if __name__ == '__main__':
    main()
