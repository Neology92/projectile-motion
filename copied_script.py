from pylab import *
import math

# Physical constants
g = 9.8
m = 1.0
rho = 1.0
Cd = 1.0
A = math.pi * pow(0.01,2.0)
alpha = rho * Cd * A / 2.0
beta = alpha / m

# Initial conditions
X0 = 1.0
Y0 = 0.0
Vx0 = 40.0
Vy0 = 80.0

# Time steps
steps = 1000
t_HIT = 2.0*Vy0/g
dt = t_HIT / steps

# No drag
X_ND = list()
Y_ND = list()

for i in range(0, steps):
  X_ND.append(X0 + Vx0 * dt * i)
  Y_ND.append(Y0 + Vy0 * dt * i - 0.5 * g * pow(dt * i,2.0))

# With drag
X_WD = list()
Y_WD = list()
Vx_WD = list()
Vy_WD = list()

for i in range(0, steps):
  X_ND.append(X0 + Vx0 * dt * i)
  Y_ND.append(Y0 + Vy0 * dt * i - 0.5 * g * pow(dt * i,2.0))

# With drag
X_WD = list()
Y_WD = list()
Vx_WD = list()
Vy_WD = list()

X_WD.append(X0)
Y_WD.append(Y0)
Vx_WD.append(Vx0)
Vy_WD.append(Vy0)

stop = 0
for i in range(1,steps+1):
  if stop != 1:
    speed = (Vx_WD[i-1]**2.0 + Vy_WD[i-1]**2.0) ** 0.5

    # First calculate velocity
    Vx_WD.append(Vx_WD[i-1] * (1.0 - beta * Vx_WD[i-1] * dt))
    Vy_WD.append(Vy_WD[i-1] + ( - g - beta * Vy_WD[i-1] * Vy_WD[i-1]) * dt)

    # Now calculate position
    X_WD.append(X_WD[i-1] + Vx_WD[i-1] * dt)
    Y_WD.append(Y_WD[i-1] + Vy_WD[i-1] * dt)

    # Stop if hits ground
    if Y_WD[i] <= 0.0:
      stop = 1

# Plot results

ylim(0,max(max(Y_WD, X_WD)))
xlim(0,max(max(Y_WD, X_WD)))
plot(X_ND, Y_ND)
plot(X_WD, Y_WD)
show()