import pgzrun
import random

WIDTH=800
HEIGHT=600
CENTER_X=WIDTH/2
CENTER_Y=HEIGHT/2
CENTER=(CENTER_X, CENTER_Y)
FINAL_LEVEL=6
START_SPEED=10

ITEMS=["bag","bottle","battery","chips"]
game_over=False
game_finished=False
current_level=1
items=[]
animations=[]

def draw():
    screen.clear()
    screen.blit("bg",(0,0))

def update():
    pass


def get_option(extra_items):
    items_to_create=["paper"]
    for i in range(extra_items):
        random_option=random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create


def create_items(items_to_create):
    new_items=[]
    for option in items_to_create:
        item=Actor(option+"img")
    new_items.append(item)
    return new_items

def layout_items(items_to_layout):
    number_of_gaps=len(items_to_layout)+1
    gap_size=WIDTH/number_of_gaps
    random.shuffle(items_to_layout)
    for index,item in enumerate(items_to_layout):
        new_x_pos=(index+1)*gap_size
        item.x=new_x_pos

def animate_items(items_to_animate):
    global animations
    for item in items_to_animate:
        duration=START_SPEED-current_level
        item.anchor=("center","bottom")
        animation=animate(item,duration=duration,on_finished=handle_game_over,y=HEIGHT)
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over=True

def on_mouse_down(pos):
    global items, current_level
    for item in items:
        if item.collidepoint(pos):
            if "paper" in item.image:
                handle_game_complete()
            else:
                handle_game_over()

def handle_game_complete():
    global current_level, items , animations , game_finished
    stop_animation()
    if current_level==FINAL_LEVEL:
        game_finished=True
    else:
        current_level+=1
        animations=[]
        items=[]

def stop_animation(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()




        





























pgzrun.go()