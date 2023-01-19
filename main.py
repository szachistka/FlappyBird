import random
import pgzrun

HEIGHT = 700
WIDTH = 400
TITLE = "Flappy Bird"
GRAVITY = 0.3
FLAP = 7
GAP_SIZE = 180
SPEED = 3


bird = Actor("bird1")
bird.x = 75
bird.y = 0
bird.vy = HEIGHT + 100
bird.points = 0
bird.dead = True

pipe_top = Actor("top")
pipe_top.anchor = ("left", "bottom")

pipe_bottom = Actor("bottom")
pipe_bottom.anchor = ("left", "top")

start = Actor("start1")
start.x = WIDTH /2
start.y = HEIGHT / 2

def draw():
    screen.blit("bg", (0,0))
    pipe_top.draw()
    pipe_bottom.draw()
    bird.draw()
    screen.draw.text(str(bird.points), center = (WIDTH / 2, 30), fontsize = 70)
    if bird.dead:
        start.draw()



def update():
    update_bird()
    update_pipes()

def update_bird():
    bird.vy += GRAVITY
    bird.y += bird.vy

    if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom) or bird.y < 0 or bird.y > HEIGHT:
        sounds.hit.play()
        bird.dead = True
        bird.image = "dead"
        bird.angle = -90

    if not bird.dead:
        if bird.vy < 0:
            bird.image = "bird2"
            bird.angle += 3
        else:
            bird.image = "bird1"
            bird.angle -= 3
        if bird.angle > 45:
            bird.angle = 45
        if bird.angle < -45:
            bird.angle = -45


def on_mouse_down(pos):
    if not bird.dead:
        bird.vy = -FLAP
        sounds.wing.play()
    elif start.collidepoint(pos):
        reset()

def on_mouse_move(pos):
    if start.collidepoint(pos):
        start.image = "start2"
    else:
        start.image = "start1"

def set_pipes():
    gap_y = random.randint(200,500)
    pipe_top.x = WIDTH
    pipe_top.y = gap_y - GAP_SIZE/2

    pipe_bottom.x = WIDTH
    pipe_bottom.y = gap_y + GAP_SIZE/2

def update_pipes():
    if bird.dead:
        return
    pipe_top.x -=SPEED
    pipe_bottom.x -= SPEED

    if pipe_top.x < -100:
        set_pipes()
        bird.points += 1
        sounds.point.play()

def reset():
    bird.x = 75
    bird.y = 200
    bird.vy = 0
    bird.points = 0
    bird.dead = False
    bird.image = "bird1"
    set_pipes()

set_pipes()
pgzrun.go()