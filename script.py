from numpy import *
from matplotlib.pyplot import *
from math import *

v = 10         # m/s
angle = 45       # degree
g = 10          # m/s^2
k = 0.24      # kg/m

def degree_to_radian(angle):
    return  angle / 180 * pi

def _input(entry, type_of):
    if type_of == 'angle':
        angle = float(input(entry))
        while (angle < 0 or angle > 90):
            print("Angle should be between 0 and 90")
            angle = float(input(entry))
        return angle
    elif type_of == 'velocity':
        v = float(input(entry))
        while (v <= 0 ):
            print("Velocity should be higher than 0")
            v = float(input(entry))
        return v
    elif type_of == 'gravity':
        g = float(input(entry))
        while (g <= 0 ):
            print("Gravity acceleration should be higher than 0")
            g = float(input(entry))
        return g
    elif type_of == 'air_resistance':
        k = float(input(entry))
        while (k < 0 ):
            print("Air resistance const cannot be less than 0")
            k = float(input(entry))
        return k
        
        


    return float(input(entry))

###############################
v = _input("Initial velocity: ", "velocity")
angle = _input("Throw angle: ", "angle")
g = _input("Earthly attraction: ", "gravity")
k = _input("Air resistance const: ", "air_resistance")
###############################


rad = degree_to_radian(angle)
vx = v * cos(rad)
vy = v * sin(rad)

dt = 0.01         #s
t = 0

x = [0]
y = [0]

stop = False
while (not stop):
    t += dt

    next_x = x[-1] + vx*dt
    next_y = y[-1] + vy*dt

    # next_x = vx*t
    # next_y = vy*t - (g*t**2)/2

    y.append(next_y)
    x.append(next_x)

    if(y[-1] <= 0):
        stop = True
    else:
        vx = vx - k*vx*dt
        vy = vy - g*dt - k*vy*dt


# def range_should_be(vo,)

max_y = max(y)
max_x = max(x)
lim = 1.1 * max(max_x, max_y)

ylim(0,lim)
xlim(-0.01*lim,lim)
plot(x, y)
show()