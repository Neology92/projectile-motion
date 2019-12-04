from numpy import *
from matplotlib.pyplot import *
from math import *

v = 20         
angle = 45       
g = 10          
k = 0.4      

def degree_to_radian(angle):
    return  angle / 180 * math.pi

rad = degree_to_radian(angle)



def foo_y(x):
    return 1/k * (v*sin(rad) + g*log(-x*k / (v*cos(rad) ) + 1)) + 1/(k**2) * (g - (g + k*v*sin(rad)) * (-x*k / (v*cos(rad) ) + 1))

def approximate_throw_range():
    return v**2 * math.sin(2*rad) / g



x = linspace(0, approximate_throw_range(), 10000)    # 51 points between 0 and 3

y = zeros(len(x))         # allocate y with float elements

for i in range(0,len(x)):
    y[i] = foo_y(x[i])

# print(x)
# print(y)


# ylim(0, ( 1.5*approximate_throw_range() if angle < 80  else 1.1*v ) )
ylim(0, 100 )
# xlim(0, ( 1.5*approximate_throw_range() if angle < 80  else 1.1*v ) )
xlim(0, 100 )
plot(x, y)
show()