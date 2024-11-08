# N - total population
# S - susceptible
# I - infected
# R - removed

# SIR model with constant total population:

# dS/dt = -b*I*S,  dI/dt = b*I*S - g*I,  dR/dt = g*I
# lets assume dt = 1day, 
# and choose random constants b and g to see what happens

import matplotlib.pyplot as plt
import Plotter
import Plot

MAX_TIME = 500 # lets simulate 500 days
N = 10_000
I = 1
S = N - I
R = 0

dt = 1
b = 0.00002
g = 0.01

# for plotting
S_data = []
I_data = []
R_data = []
days = [] 

for i in range(MAX_TIME):
  dS = -b*I*S * dt
  dI = ( b*I*S - g*I ) * dt
  dR = g*I * dt
  S += dS
  I += dI
  R += dR
  
  if S < 0:
    S = 0
  if I < 0:
    I = 0
  if R < 0:
    R = 0
  
  S_data.append(S)
  I_data.append(I)
  R_data.append(R)
  days.append(i)

plt.plot(days, S_data, label='Susceptible')
plt.plot(days, I_data, label='Infected')
plt.plot(days, R_data, label='Removed')
# plt.ylim(0, N)
# plt.yscale("log")
# plt.xscale("log")
plt.legend()
plt.show()
