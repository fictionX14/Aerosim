# main.py

from config import MASS, GRAVITY, TIME_STEP, SIM_TIME, THRUST, ANGLE
from dynamics import update_state
import matplotlib.pyplot as plt

#initial state: [x, y, vx, vy]
# x and y are positions, vx and vy are velocities
# Initializing state
state = [0.0, 0.0, 0.0, 0.0] 

# Logging data for plotting
trajectory = []

# Simulation Loop
time = 0.0
while time <= SIM_TIME:
    trajectory.append((time, *state))
    state = update_state(MASS, GRAVITY, state, THRUST, ANGLE, TIME_STEP)
    time += TIME_STEP

# Plotting the trajectory
xvals = [pos[1] for pos in trajectory]
yvals = [pos[2] for pos in trajectory]

plt.plot(xvals, yvals)
plt.title('Missle Trajectory')
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.grid(True)
plt.savefig('trajectory.png')
