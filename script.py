from numpy import *
from matplotlib.pyplot import *
from math import *

v = 300         # m/s
angle = 45       # degree
g = 10          # m/s^2
k = -0.24      # kg/m

def degree_to_radian(angle):
    # return  angle / 180 * math.pi
    return  angle 

rad = degree_to_radian(angle)


def foo_x(t):   
    # return Vo * math.cos(rad) / res * (1 - math.e**(-res  * t))
    return (v*cos(rad) / k) * ( 1 - e**(-k*t) ) 

def foo_y(t):
    # return (( Vo * math.sin(rad) + g) * (1 - math.e**(-res  * t)) - g*t)/res
    return 1/k + (v*sin(rad) - g*t) + (1/k**2) * (g - e**(-k*t) * ( g + k*v*sin(rad) ))

def time_to_back_on_earth():
    return 2*v * math.sin(rad)/g

def throw_range():
    return foo_x(time_to_back_on_earth())


t = linspace(0, 100, 201)    

y = zeros(len(t))         # allocate y with float elements
x = zeros(len(t))         # allocate y with float elements

for i in range(0,len(t)):
    y[i] = foo_y(t[i])
    x[i] = foo_x(t[i])


# ylim(0,1.5*throw_range())
# xlim(0,1.5*throw_range())
plot(x, y)
show()