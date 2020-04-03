from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import time



class Controller(object):
    def __init__(self, drone):
        self.sense = SenseHat()
        self.drone = drone
        self.landed = True
        #self.sense.set_imu_config(False, True, False)

        self.sense.stick.direction_up = self.pushed_up
        self.sense.stick.direction_middle = self.pushed_middle
        self.sense.stick.direction_down = self.pushed_down
    
    def pushed_middle(self, event):
        if (event.action != ACTION_RELEASED):
            #print("Midten er trykket")
            self.sense.set_pixels(poin_hal)
            self.drone.stop()

    def pushed_up(self, event):
        if (event.action == ACTION_HELD and self.landed):
            #print("Op er trykket")
            self.sense.set_pixels(poin_up)
            self.drone.takeOff()
            self.landed = False
    
    def pushed_down(self, event):
        if (event.action == ACTION_HELD and not self.landed):
            self.sense.set_pixels(poin_down)
            self.drone.land()
            self.landed = True
    
    def check_roll(self):
        roll = self.sense.get_gyroscope()['roll']
        if (roll >= 45.0 and roll < 90.0):
            self.drone.ascend_alt(20)
            #time.sleep(0.5)
        elif (roll <= 315.0 and roll > 270.0):
            self.drone.descend_alt(20)
            #time.sleep(0.5)
    
    def check_pitch(self):
        pitch = self.sense.get_gyroscope()['pitch']
        if (pitch >= 45.0 and pitch < 90.0):
            self.drone.ccw(5)
            #time.sleep(0.5)
        elif (pitch <= 315.0 and pitch > 270.0):
            self.drone.cw(5)
            #time.sleep(0.5)

    


    
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
