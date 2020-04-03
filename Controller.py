from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import Drone


class Controller(object):
    def __init__(self, drone):
        self.sense = SenseHat()
        self.drone = drone

        self.sense.stick.direction_up = self.pushed_up
        self.sense.stick.direction_middle = self.pushed_middle
    
    def pushed_middle(event):
        if (event.action != ACTION_RELEASED):
            drone.stop()

    def pushed_up(event):
        if (event.action == ACTION_RELEASED):
            drone.takeOff()
    

    
# colours defined
r = (255, 0, 0) # red
g = (0, 255, 0) # Green
y = (255, 255, 0) # Yellow
o = (0, 0, 0) # Black

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





def repeat():
    global temp
    newtemp = round (temp, 1)

    if (temp > 35):
	    sense.set_pixels(temp_pixel35)