from numpy import *
from matplotlib.pyplot import *
from math import *

# def _input(entry, type_of):
#     if type_of == 'angle':
#         angle = float(input(entry))
#         while (angle < 0 or angle > 90):
#             print("Angle should be between 0 and 90")
#             angle = float(input(entry))
#         return angle
#     elif type_of == 'velocity':
#         v = float(input(entry))
#         while (v <= 0 ):
#             print("Velocity should be higher than 0")
#             v = float(input(entry))
#         return v
#     elif type_of == 'gravity':
#         g = float(input(entry))
#         while (g <= 0 ):
#             print("Gravity acceleration should be higher than 0")
#             g = float(input(entry))
#         return g
#     elif type_of == 'air_resistance':
#         k = float(input(entry))
#         while (k < 0 ):
#             print("Air resistance const cannot be less than 0")
#             k = float(input(entry))
#         return k        

def degree_to_radian(angle):
    return  angle / 180 * pi

def calcxy(v, dt, k, g, angle ):

    # Calc x and y velocity
    rad = degree_to_radian(angle)
    vx = v * cos(rad)
    vy = v * sin(rad)

    x = [0]
    y = [0]
    stop = False
 
    while (not stop):

        # Calculate next position
        next_x = x[-1] + vx*dt
        next_y = y[-1] + vy*dt

        y.append(next_y)
        x.append(next_x)

        # Calculate next step velocoty
        vx = vx - k*vx*dt
        vy = vy - g*dt - k*vy*dt

        if(y[-1] <= 0):
            stop = True

    return (x,y)


####################
#       Init
# ------------------
v = 80           # m/s
angle = 45       # degree
g = 10           # m/s^2
k = 0.24         # kg/m

# time step
dt = 0.01        # s


####################
#   Calculate values
# ------------------
x,y = calcxy(v, dt, k, g, angle)


####################
#   Set margins
# ------------------
subplots_adjust(left=0.15, bottom=0.3)
l, = plot(x, y, lw=2)


######################
#   Sliders
# --------------------
axcolor = '#EEEEEE'
ax_v = axes([0.2, 0.17, 0.65, 0.03], facecolor=axcolor)
ax_a = axes([0.2, 0.12, 0.65, 0.03], facecolor=axcolor)
ax_g = axes([0.2, 0.07, 0.65, 0.03], facecolor=axcolor)
ax_k = axes([0.2, 0.02, 0.65, 0.03], facecolor=axcolor)
ax_none = axes([0, 0, 0.0, 0.0], facecolor=axcolor)

s_v = Slider(ax_v, 'Velocity', 0.1, 80.0, valinit=v, valstep=0.01)
s_a = Slider(ax_a, 'Angle', 0.1, 90.0, valinit=angle, valstep=0.1)
s_g = Slider(ax_g, 'Gravity', 5.0, 50.0, valinit=g, valstep=0.01)
s_k = Slider(ax_k, 'Air res', 0, 1.0, valinit=k, valstep=0.001)
s_none = Slider(ax_none, '', 0, 0.1, valinit=0, valstep=0.01)


#####################
#   Update from slider
# -------------------
def update(val):
    v = s_v.val
    angle = s_a.val
    g = s_g.val
    k = s_k.val
    x,y = calcxy(v, dt, k, g, angle)
    l.set_xdata(x)
    l.set_ydata(y)
    # fig.canvas.draw_idle()

s_v.on_changed(update)
s_a.on_changed(update)
s_g.on_changed(update)
s_k.on_changed(update)


#####################
#   Set chart limits
# -------------------

max_y = max(y)
max_x = max(x)
lim = 1.1 * max(max_x, max_y)

ylim(0,lim)
xlim(-0.01*lim,lim)

####################
#   Draw chart
# ------------------
plot(x, y)
draw()
show()