from numpy import *
from matplotlib.pyplot import *
import math

Vo = 20         # m/s
angle = 89.99       # degree
g = 10          # m/s^2
res = 0.24      # kg/m
# res = 0      # kg/m

def degree_to_radian(angle):
    return  angle / 180 * math.pi

rad = degree_to_radian(angle)



def foo_y(x):
    return (-1/2) * (g / (Vo**2 * math.cos(rad)**2) ) * x**2 + math.tan(rad) * x

def throw_range():
    return Vo**2 * math.sin(2*rad) / g



x = linspace(0, throw_range(), 10000)    # 51 points between 0 and 3

y = zeros(len(x))         # allocate y with float elements

for i in range(0,len(x)):
    y[i] = foo_y(x[i])


ylim(0, ( 1.5*throw_range() if angle < 80  else 1.1*Vo ) )
xlim(0, ( 1.5*throw_range() if angle < 80  else 1.1*Vo ) )
plot(x, y)
show()