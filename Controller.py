from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import Drone


class Controller(object):
    def __init__(self, drone):
        self.sense = SenseHat()
        self.drone = drone

        self.sense.stick.direction_up = self.pushed_up
        self.sense.stick.direction_middle = self.pushed_middle
        self.sense.stick.direction_down = self.pushed_down
    
    def pushed_middle(self, event):
        if (event.action != ACTION_RELEASED):
            #print("Midten er trykket")
            self.sense.set_pixels(poin_hal)
            self.drone.stop()

    def pushed_up(self, event):
        if (event.action != ACTION_RELEASED):
            #print("Op er trykket")
            self.sense.set_pixels(poin_up)
            self.drone.takeOff()
    
    def pushed_down(self, event):
        if (event.action != ACTION_RELEASED):
            self.sense.set_pixels(poin_down)
            self.drone.land()
    
    def check_yaw(self):
        yaw = self.sense.get_orientation()
    


    
# colours defined
r = (255, 0, 0) # red
g = (0, 255, 0) # Green
y = (255, 255, 0) # Yellow
o = (0, 0, 0) # Black
w = (255, 255, 255) # White

#farve matrixer

bat_green = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g
]

bat_yel = [
    y, y, y, y, y, y, y, y,
    y, y, y, y, y, y, y, y,
    y, y, y, y, y, y, y, y,
    y, y, y, y, y, y, y, y,
    y, y, y, y, y, y, y, y,
    y, y, y, y, y, y, y, y,
    y, y, y, y, y, y, y, y,
    y, y, y, y, y, y, y, y
]

bat_red = [
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r
]

# Pile

poin_up = [
    o, o, o, w, w, o, o, o,
    o, o, w, w, w, w, o, o,
    o, w, w, w, w, w, w, o,
    o, w, o, w, w, o, w, o,
    o, o, o, o, o, o, o, o,
    o, o, o, w, w, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, w, w, o, o, o
]

poin_down = [
    o, o, o, w, w, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, w, w, o, o, o,
    o, o, o, o, o, o, o, o,
    o, w, o, w, w, o, w, o,
    o, w, w, w, w, w, w, o,
    o, o, w, w, w, w, o, o,
    o, o, o, w, w, o, o, o
]

poin_hal = [
    o, o, o, o, o, o, o, o,
    o, o, w, w, w, w, o, o,
    o, w, w, o, o, w, w, o,
    o, w, o, o, o, o, w, o,
    o, w, o, o, o, o, w, o,
    o, w, w, o, o, w, w, o,
    o, o, w, w, w, w, o, o,
    o, o, o, o, o, o, o, o
]






#from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
#from signal import pause

#x = 3
#y = 3
#sense = SenseHat()

def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

def pushed_up(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y - 1)

def pushed_down(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y + 1)

def pushed_left(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x - 1)

def pushed_right(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x + 1)

def refresh():
    sense.clear()
    sense.set_pixel(x, y, 255, 255, 255)

#sense.stick.direction_up = pushed_up
#sense.stick.direction_down = pushed_down
#sense.stick.direction_left = pushed_left
#sense.stick.direction_right = pushed_right
#sense.stick.direction_any = refresh
#refresh()
#pause()