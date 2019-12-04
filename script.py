from numpy import *
from matplotlib.pyplot import *
import math

Vo = 300         # m/s
angle = 45       # degree
g = 10          # m/s^2
res = 0.24      # kg/m
# res = 0      # kg/m

def degree_to_radian(angle):
    return  angle / 180 * math.pi

rad = degree_to_radian(angle)


def foo_x(t):   
    return Vo * math.cos(rad) / res * (1 - math.e**(-res  * t))

def foo_y(t):
    return (( Vo * math.sin(rad) + g) * (1 - math.e**(-res  * t)) - g*t)/res

def time_to_back_on_earth():
    return 2*Vo * math.sin(rad)/g

def throw_range():
    return foo_x(time_to_back_on_earth())


t = linspace(0, time_to_back_on_earth(), 10000)    # 51 points between 0 and 3

y = zeros(len(t))         # allocate y with float elements
x = zeros(len(t))         # allocate y with float elements

for i in range(0,len(t)):
    y[i] = foo_y(t[i])
    x[i] = foo_x(t[i])


ylim(0,1.5*throw_range())
xlim(0,1.5*throw_range())
plot(x, y)
show()